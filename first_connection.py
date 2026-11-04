
import time
import pycozmo

print("===================================")
print("       COZMO REBORN")
print("   First Hardware Connection Test")
print("===================================")

print("\nConnecting to Cozmo...")

try:
    with pycozmo.connect() as cozmo:

        print("Connected to Cozmo!")
        print("Sending first movement command...")

        # Move Cozmo's head slightly upwards
        cozmo.set_head_angle(angle=0.3)

        time.sleep(2)

        # Return the head to its neutral position
        cozmo.set_head_angle(angle=0.0)

        time.sleep(2)

        print("\nFirst movement test completed!")

except Exception as error:
    print("\nConnection test failed.")
    print("Error:", error)

print("\nCozmo Reborn test finished.")
