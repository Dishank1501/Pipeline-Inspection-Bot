import cv2
import numpy as np

# ==========================================
# PIPELINE CRACK DETECTION USING OPENCV
# Ubuntu 20.04 | Python 3 | IP Camera
# ==========================================

# Replace with your IP camera URL
CAMERA_URL = "http://192.168.0.101:8080/video"

# Detection parameters
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

CANNY_LOW = 30
CANNY_HIGH = 90

MIN_CONTOUR_AREA = 20

# Connect to the IP camera
cap = cv2.VideoCapture(CAMERA_URL)

if not cap.isOpened():
    print("ERROR: Cannot connect to IP camera.")
    print("Check the camera URL and network connection.")
    raise SystemExit(1)

# Improve contrast in low-light pipeline environments
clahe = cv2.createCLAHE(
    clipLimit=3.0,
    tileGridSize=(8, 8)
)

# Morphological kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (3, 3)
)

print("Pipeline Crack Detection Started")
print("Press Q to quit.")

try:
    while True:

        # Capture frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to receive frame from camera.")
            break

        # Resize frame
        frame = cv2.resize(
            frame,
            (FRAME_WIDTH, FRAME_HEIGHT)
        )

        # Convert to grayscale
        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        # Enhance local contrast
        enhanced = clahe.apply(gray)

        # Reduce noise while preserving edges
        blurred = cv2.GaussianBlur(
            enhanced,
            (3, 3),
            0
        )

        # Detect edges
        edges = cv2.Canny(
            blurred,
            CANNY_LOW,
            CANNY_HIGH
        )

        # Connect small gaps in crack edges
        closed = cv2.morphologyEx(
            edges,
            cv2.MORPH_CLOSE,
            kernel,
            iterations=1
        )

        # Find contours
        contours, _ = cv2.findContours(
            closed.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        output = frame.copy()
        crack_count = 0

        for contour in contours:

            area = cv2.contourArea(contour)

            # Ignore small contours
            if area < MIN_CONTOUR_AREA:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            # Filter for elongated features
            aspect_ratio = max(w, h) / float(min(w, h))

            if aspect_ratio >= 2.0:

                crack_count += 1

                # Draw detected candidate in red
                cv2.drawContours(
                    output,
                    [contour],
                    -1,
                    (0, 0, 255),
                    1
                )

                # Draw bounding box
                cv2.rectangle(
                    output,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    1
                )

        # Display candidate count
        cv2.putText(
            output,
            f"Crack-like candidates: {crack_count}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 255, 0),
            2
        )

        # Display windows
        cv2.imshow(
            "Pipeline Crack Detection",
            output
        )

        cv2.imshow(
            "Enhanced Image",
            enhanced
        )

        cv2.imshow(
            "Edge Detection",
            closed
        )

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

print("Pipeline Crack Detection Stopped.")
