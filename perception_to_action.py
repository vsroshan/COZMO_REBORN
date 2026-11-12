
import time
from pathlib import Path

import pycozmo
from ultralytics import YOLO

print("===================================")
print("          COZMO REBORN")
print(" Experiment 005: Perception to Action")
print("===================================")

IMAGE_PATH = Path("camera_capture.png")
MODEL_PATH = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.50

if not IMAGE_PATH.exists():
    raise FileNotFoundError(
        "camera_capture.png is missing. "
        "Complete Experiment 002 first."
    )

print("\nLoading AI vision model...")
model = YOLO(MODEL_PATH)

print("Analysing Cozmo's camera image...")
results = model(str(IMAGE_PATH))
result = results[0]

detected_person = False

print("\nDetected objects:")

for box in result.boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    label = model.names[class_id]

    if confidence < CONFIDENCE_THRESHOLD:
        continue

    print(f"- {label}: {confidence:.2%}")

    if label == "person":
        detected_person = True

print("\nDecision:")

if detected_person:
    print("Person detected!")
    print("Action: Raise Cozmo's head.")
    target_angle = 0.3
else:
    print("No person detected with sufficient confidence.")
    print("Action: Return head to neutral position.")
    target_angle = 0.0

print("\nConnecting to Cozmo...")

try:
    with pycozmo.connect() as cozmo:
        print("Connected successfully!")

        cozmo.set_head_angle(angle=target_angle)
        time.sleep(2)

        print("\nPhysical action completed!")

except Exception as error:
    print("\nRobot connection failed.")
    print("Error:", error)

print("\nExperiment 005 finished!")
