# Cozmo Reborn
### Open Research in Resource-Aware Embodied Intelligence

An open research project exploring resource-aware embodied intelligence and modular AI architectures on legacy robotic platforms.

Cozmo Reborn investigates how small, resource-constrained robots can perceive their surroundings, make decisions, interact with the physical world and adapt through experience.

Rather than building another conversational robot, this project focuses on the engineering and research challenges behind reliable, adaptive physical intelligence.

---

## Research Question

**How can resource-constrained robotic systems achieve reliable, adaptive and context-aware physical behaviour through modular, open-source AI architectures?**

## Research Areas

1. **Resource-Aware Intelligence** — Local and cloud inference, computational constraints, latency and offline resilience.
2. **Closed-Loop Physical Reasoning** — Perception, interpretation, action and feedback.
3. **Uncertainty-Aware Autonomy** — Recognising uncertainty and making safe decisions.
4. **Learning from Physical Experience** — Episodic memory, experience logging and behavioural adaptation.
5. **Hardware-Independent Architecture** — Modular AI components that can extend across robotic platforms.

---

## Hardware Platform

The initial platform is the original Anki Cozmo robot.

| Component | Purpose |
|---|---|
| Original Anki Cozmo | Physical robotic platform |
| Cozmo camera | Visual input |
| Motors and actuators | Physical movement |
| Microphone | Future audio experimentation |
| MacBook Pro | Primary development environment |
| Raspberry Pi 3 | Potential future edge-computing platform |

The project uses PyCozmo, an independent community-developed Python implementation, to communicate with the original Cozmo hardware.

---

## Technology Stack

- Python
- PyCozmo
- OpenCV
- NumPy
- Ultralytics YOLO
- Computer Vision
- Robotics and Control Systems
- Edge AI
- Resource-Constrained Computing

---

## Development Progress

### Experiment 001 — Direct Hardware Connection

**Status: Completed**

Established direct communication between the development machine and the original Cozmo robot using PyCozmo.

Implemented:
- Python virtual environment setup.
- PyCozmo installation.
- Direct robot communication.
- Head-position commands.
- Physical actuator testing.

**Result:** Cozmo successfully moved its head in response to Python commands.

### Experiment 002 — Camera Capture

**Status: In Progress**

**Objective:** Establish a visual data acquisition pipeline using Cozmo's onboard camera.

Planned implementation:
- Enable the camera.
- Receive camera image data.
- Capture and save an image.
- Verify image quality and resolution.

Expected output: `camera_capture.png`

### Experiment 003 — Computer Vision Pipeline

**Status: In Progress**

**Objective:** Process visual input using OpenCV and NumPy.

Planned implementation:
- Load the camera image.
- Resize and preprocess the image.
- Convert the image to grayscale.
- Apply Gaussian blur.
- Perform Canny edge detection.
- Calculate edge density.
- Save processed outputs.

Expected outputs:
- `resized.png`
- `grayscale.png`
- `edges.png`
- `comparison.png`

**Technical note:** Edge detection identifies visual boundaries. It does not independently identify objects or understand a scene.

### Experiment 004 — AI-Based Object Detection

**Status: In Progress**

**Objective:** Explore AI-based object recognition using YOLO.

Planned implementation:
- Load a Cozmo camera image.
- Load the YOLOv8 Nano model.
- Run object detection.
- Identify recognised object classes.
- Retrieve confidence scores.
- Generate annotated images with bounding boxes.

Expected output:

`detection_output/detected_objects.png`

**Current limitation:** This experiment analyses a saved image rather than a live camera stream.

### Experiment 005 — Perception-to-Action

**Status: In Progress**

**Objective:** Connect AI-based visual recognition to physical robot behaviour.

Implementation:
- Load an image captured by Cozmo.
- Run YOLO object detection.
- Identify whether a person is detected.
- Apply a confidence threshold.
- Select a corresponding robot action.
- Send a head-position command to Cozmo.

**Decision logic:**

| Detection result | Robot response |
|---|---|
| Person detected above confidence threshold | Raise head |
| No qualifying person detected | Return head to neutral position |

**Architecture:**

Visual Input → AI Perception → Decision Logic → Physical Action

**Research significance:** Introduces an initial connection between machine perception and physical actuator commands.

**Current limitation:** Uses a previously captured image. It is not yet continuous, real-time or closed-loop autonomous behaviour.

### Experiment 006 — Spatial Perception & Adaptive Head Positioning

**Status: In Progress**

**Objective:** Explore how the spatial position of a detected person can influence a robot's physical response.

This experiment extends basic object detection by using the vertical location of a detected person's bounding box.

**Implementation:**
- Load a previously captured Cozmo camera image.
- Run YOLO person detection.
- Identify the largest qualifying person detection.
- Calculate the vertical centre of the bounding box.
- Normalise the position relative to image height.
- Calculate a target head angle.
- Apply a centre dead zone.
- Send the calculated head-position command to Cozmo.
- Save an annotated detection image.

**Decision logic:**

| Person's vertical position | Intended robot response |
|---|---|
| Upper image region | Raise head |
| Centre region | Keep head near neutral |
| Lower image region | Lower head |
| No qualifying person detected | Return head to neutral |

**Core architecture:**

Visual Input → Object Detection → Spatial Analysis → Action Selection → Physical Movement

**Research significance:**

Introduces spatially informed action selection. Instead of responding only to an object's presence, the robot uses information about where the object appears in the image.

**Expected output:**

`spatial_output/spatial_detection.png`

**Current limitations:**
- Uses a saved image rather than live camera input.
- Only processes person detections.
- Does not perform continuous person tracking.
- Does not yet use feedback to correct movement.
- Head-position mapping is experimental and requires physical calibration.
- Does not yet implement autonomous behavioural adaptation.

---

## Repository Structure

```text
cozmo-reborn/
│
├── first_connection.py
├── camera_capture.py
├── vision_analysis.py
├── object_detection.py
├── perception_to_action.py
├── spatial_attention.py
│
├── vision_output/
├── detection_output/
├── spatial_output/
│
├── docs/
│   └── evidence/
│
├── DEVLOG.md
├── README.md
├── .gitignore
└── requirements.txt
```

The repository structure will evolve as additional modules and experiments are introduced.

---

## Development Philosophy

Cozmo Reborn follows an experiment-driven and modular development approach.

Each experiment aims to:

- Address a specific technical question.
- Produce a reproducible implementation.
- Validate behaviour through observable results.
- Document limitations and failures.
- Build towards a larger integrated architecture.

Verified results are distinguished from ongoing experiments and future research objectives.

---

## Long-Term Vision

The long-term objective is to develop an open, modular embodied intelligence architecture that can operate across constrained robotic platforms.

Potential future capabilities include:

- Visual perception and scene understanding.
- Object detection and recognition.
- Spatial awareness and object tracking.
- Context-aware physical interaction.
- Real-time perception and feedback.
- Closed-loop movement and control.
- Local AI inference and edge computing.
- Memory-based adaptation.
- Uncertainty-aware decision-making.
- Cross-platform robotic experimentation.

These are future research directions, not claims of existing functionality.

---

## Open Research

Cozmo Reborn is an evolving independent research and engineering project.

The intention is to document the process openly, publish reproducible experiments, evaluate system behaviour and contribute to the broader exploration of embodied intelligence.

**The objective is not simply to make a robot respond. It is to investigate how a robot can perceive, reason, act and learn within the constraints of the physical world.**

---

**Project:** Cozmo Reborn  
**Focus:** Resource-Aware Embodied Intelligence  
**Status:** Active Development





