
import cv2
import numpy as np
from pathlib import Path

print("===================================")
print("          COZMO REBORN")
print("   Experiment 003: Computer Vision")
print("===================================")

# Project paths
image_path = Path("camera_capture.png")
output_dir = Path("vision_output")
output_dir.mkdir(exist_ok=True)

# 1. Load Cozmo's camera image
print("\nLoading camera image...")

if not image_path.exists():
    raise FileNotFoundError(
        "camera_capture.png not found. "
        "Run Experiment 002 first."
    )

image = cv2.imread(str(image_path))

if image is None:
    raise ValueError("Unable to decode the camera image.")

height, width, channels = image.shape

print("Image loaded successfully!")
print(f"Resolution: {width} x {height}")
print(f"Channels: {channels}")

# 2. Resize image
resized = cv2.resize(image, (640, 480))

# 3. Convert to grayscale
grayscale = cv2.cvtColor(
    resized,
    cv2.COLOR_BGR2GRAY
)

# 4. Apply Gaussian blur
blurred = cv2.GaussianBlur(
    grayscale,
    (5, 5),
    0
)

# 5. Detect edges using Canny
edges = cv2.Canny(
    blurred,
    50,
    150
)

# 6. Calculate edge density
edge_pixels = np.count_nonzero(edges)
total_pixels = edges.size

edge_density = (edge_pixels / total_pixels) * 100

print("\nImage analysis completed!")
print(f"Detected edge pixels: {edge_pixels}")
print(f"Edge density: {edge_density:.2f}%")

# 7. Save processed images
cv2.imwrite(
    str(output_dir / "resized.png"),
    resized
)

cv2.imwrite(
    str(output_dir / "grayscale.png"),
    grayscale
)

cv2.imwrite(
    str(output_dir / "edges.png"),
    edges
)

# 8. Create a combined visualisation
edge_visual = cv2.cvtColor(
    edges,
    cv2.COLOR_GRAY2BGR
)

comparison = np.hstack((
    resized,
    edge_visual
))

cv2.imwrite(
    str(output_dir / "comparison.png"),
    comparison
)

print("\nSaved results:")
print("- vision_output/resized.png")
print("- vision_output/grayscale.png")
print("- vision_output/edges.png")
print("- vision_output/comparison.png")

print("\nExperiment 003 completed!")
