
import time
import pycozmo

print("===================================")
print("          COZMO REBORN")
print(" Experiment 007: Head Calibration")
print("===================================")

# Small test angles in radians.
# These are deliberately conservative test positions.
TEST_ANGLES = [
    0.00,
    0.10,
    0.20,
    0.30,
    0.20,
    0.10,
    0.00,
    -0.10,
    -0.20,
    -0.10,
    0.00
]

SETTLE_TIME = 1.5

print("\nCalibration sequence:")
for index, angle in enumerate(TEST_ANGLES, start=1):
    print(f"{index}. {angle:.2f} radians")

print("\nConnecting to Cozmo...")

try:
    with pycozmo.connect() as cozmo:
        print("Connected successfully!")

        for index, angle in enumerate(TEST_ANGLES, start=1):
            print(
                f"\nMovement {index}/{len(TEST_ANGLES)}"
            )
            print(f"Target angle: {angle:.2f} radians")

            cozmo.set_head_angle(angle=angle)

            time.sleep(SETTLE_TIME)

            print("Command sent.")

        print("\nReturning Cozmo to neutral position...")
        cozmo.set_head_angle(angle=0.0)
        time.sleep(2)

        print("\nCalibration sequence completed!")

except KeyboardInterrupt:
    print("\nCalibration interrupted by user.")

except Exception as error:
    print("\nCalibration failed.")
    print("Error:", error)

print("\nExperiment 007 finished!")
