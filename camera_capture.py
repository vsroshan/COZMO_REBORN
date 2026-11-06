
import time
import pycozmo

print("===================================")
print("       COZMO REBORN")
print("   Experiment 002: Camera Capture")
print("===================================")

def on_camera_image(cli, image):
    """Save the first image received from Cozmo."""
    image.save("camera_capture.png", "PNG")
    print("\nSUCCESS! Camera image received.")
    print("Saved as: camera_capture.png")


try:
    print("\nConnecting to Cozmo...")

    with pycozmo.connect() as cli:

        print("Connected successfully!")

        # Raise Cozmo's head slightly
        angle = (
            pycozmo.robot.MAX_HEAD_ANGLE.radians
            - pycozmo.robot.MIN_HEAD_ANGLE.radians
        ) / 2.0

        cli.set_head_angle(angle)

        # Enable the colour camera
        cli.enable_camera(enable=True, color=True)

        print("Camera enabled. Waiting for stabilisation...")

        time.sleep(2)

        # Listen for the first camera image
        cli.add_handler(
            pycozmo.event.EvtNewRawCameraImage,
            on_camera_image,
            one_shot=True
        )

        print("Waiting for camera image...")

        time.sleep(3)

    print("\nExperiment 002 finished.")

except Exception as error:
    print("\nCAMERA TEST FAILED")
    print("Error:", error)

