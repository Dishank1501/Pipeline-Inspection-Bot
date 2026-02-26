🚀 Pipeline Inspection & Crack Healing Robot
An autonomous 4WD pipeline inspection robot designed for 6-inch sewage pipelines, capable of detecting cracks using OpenCV and healing them using a robotic syringe injector mechanism.
📌 Project Overview
This robot is built for pipeline inspection, crack detection, and minor crack repair in confined sewage pipelines.

It uses:
🎥-   Raspberry Pi Camera for real-time video feed
🧠-   OpenCV for crack detection
💉-   Robotic arm with syringe injector for crack healing
💡-   High-intensity LEDs for low-light environments
🛞-   4WD N20 motor drive system for stable movement
The system is designed with a fully enclosed electronics compartment and a removable top cover for maintenance.

🛠 Hardware Components
🍓-   Raspberry Pi Zero 2 W
📷-   Raspberry Pi Camera Module
⚙️-   4 × N20 DC Motors (5cm wheels)
🔌-   L298N Motor Driver
🔋-   3 × 18650 Li-ion Batteries
💡-   4 × Front LEDs
🤖-   SG90 Servo Motors (for robotic arm)
💉-   Syringe-based crack injection system
🧱-   Custom 3D printed chassis (fits 6-inch pipeline)

🧠 Software Stack
-  Python 3
-  OpenCV
-  Flask (for local web control)
-  Raspberry Pi OS
-  GPIO Control Libraries

🔍 Crack Detection Method
The robot uses OpenCV image processing techniques:
-  Grayscale conversion
-  Gaussian Blur
-  Canny Edge Detection
-  Contour Detection
-  morphological operations

When a crack is detected:
The robot stops.
The robotic arm positions the syringe.
Sealant material is injected into the crack.
