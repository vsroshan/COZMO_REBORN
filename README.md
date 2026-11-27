# Cozmo Reborn
### Open Research in Resource-Aware Embodied Intelligence

**Cozmo Reborn** is an open research project exploring resource-aware embodied intelligence and modular AI architectures on legacy robotic platforms.

The project uses the original Anki Cozmo robot as an experimental platform to investigate how physical robots can perceive their surroundings, interpret information, make decisions, and interact with the physical world despite limited hardware resources.

---

## Research Question

**How can resource-constrained robotic systems achieve reliable, adaptive and context-aware physical behaviour through modular, open-source AI architectures?**

Rather than simply building another conversational robot, Cozmo Reborn investigates the engineering and research foundations of embodied intelligence.

## Core Research Areas

1. **Resource-Aware Intelligence** — Exploring local and cloud inference, latency, connectivity, offline resilience, and computational constraints.
2. **Closed-Loop Physical Reasoning** — Connecting perception, state estimation, decision-making, physical action, and observation of outcomes.
3. **Uncertainty-Aware Autonomy** — Investigating how robots can recognise uncertainty, gather more information, request human input, and choose safer actions.
4. **Learning from Physical Experience** — Exploring memory, experience logging, adaptation, and recovery from failures.
5. **Hardware-Independent Architecture** — Developing modular systems that could eventually extend beyond Cozmo to other robotic platforms.

## Hardware Platform

**Primary platform:** Original Anki Cozmo robot.

- Original Cozmo hardware
- Integrated camera
- Head movement actuator
- Differential-drive movement system
- Built-in sensors

The project currently uses PyCozmo, an independent community-developed Python implementation that communicates directly with Cozmo.

Additional platforms may be explored in future research.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| PyCozmo | Cozmo hardware communication |
| OpenCV | Computer vision |
| NumPy | Image and numerical processing |
| Ultralytics YOLO | AI-based object detection |
| GitHub | Open-source development and documentation |

---

## Development Progress

The project follows an incremental experimental approach. Each experiment explores one capability before building on it.

### Experiment 001 — Direct Hardware Connection

**Status: Verified**

Established direct communication between Python and the original Cozmo robot using PyCozmo.

Objectives:
- Establish a hardware connection.
- Send head movement commands.
- Verify physical actuator response.

Outcome:
- Successfully connected to Cozmo.
- Successfully controlled the head actuator.
- Confirmed physical movement from Python commands.

File: `first_connection.py`

### Experiment 002 — Camera Capture

**Status: In Progress**

Investigating access to Cozmo's onboard camera through PyCozmo.

Objectives:
- Enable the camera stream.
- Receive camera image events.
- Capture and save an image.
- Establish a visual input pipeline.

File: `camera_capture.py`

Expected output: `camera_capture.png`

### Experiment 003 — Computer Vision Pipeline

**Status: In Progress**

Building an initial image-processing pipeline using OpenCV.

Objectives:
- Load a captured camera image.
- Resize and preprocess the image.
- Convert the image to grayscale.
- Apply Gaussian blur.
- Detect edges using Canny edge detection.
- Calculate basic image statistics.

Expected outputs:
- `vision_output/resized.png`
- `vision_output/grayscale.png`
- `vision_output/edges.png`
- `vision_output/comparison.png`

File: `vision_analysis.py`

### Experiment 004 — AI Object Detection

**Status: In Progress**

Introducing AI-based object detection using YOLO.

Objectives:
- Load an image captured by Cozmo.
- Run object detection using a pretrained YOLO model.
- Identify recognised object classes.
- Record detection confidence scores.
- Generate an annotated image.

Expected output: `detection_output/detected_objects.png`

File: `object_detection.py`

### Experiment 005 — Perception-to-Action

**Status: In Progress**

Exploring the connection between visual perception and physical behaviour.

Objectives:
- Process a captured camera image.
- Detect a person using YOLO.
- Evaluate the detection confidence.
- Select a head movement based on the detection result.
- Send the selected movement command to Cozmo.

This experiment introduces a basic perception-driven action pipeline. It currently uses a saved image rather than continuous live perception.

File: `perception_to_action.py`

### Experiment 006 — Spatial Perception & Adaptive Head Positioning

**Status: In Progress**

Exploring how spatial information from object detection can influence physical positioning.

Objectives:
- Detect a person in an image.
- Extract the bounding box coordinates.
- Calculate the vertical centre of the detected person.
- Normalise the person's position within the image.
- Map the spatial position to a target head angle.
- Command Cozmo's head actuator.

Expected output: `spatial_output/spatial_detection.png`

This experiment explores spatially informed action selection using a captured image. It does not yet implement continuous visual tracking or closed-loop autonomy.

File: `spatial_attention.py`

### Experiment 007 — Head Actuator Calibration & Repeatability

**Status: In Progress**

Establishing a baseline for Cozmo's head actuator through controlled movement commands.

Objectives:
- Test a sequence of small head-angle commands.
- Observe movement across positive and negative angles.
- Examine repeatability across repeated target positions.
- Return the actuator to a neutral position.
- Establish a baseline for future perception-driven movement experiments.

The current experiment records commanded angles and allows physical observation. It does not independently measure the actual actuator position.

File: `head_calibration.py`

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
├── head_calibration.py
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
├── requirements.txt
└── .gitignore
```

*Generated output folders and evidence directories will be added as the corresponding experiments produce results.*

## Development Philosophy

Cozmo Reborn follows five principles:

- **Incremental experimentation:** Build and validate one capability at a time.
- **Measurable progress:** Record observations, results, limitations, and failures.
- **Modular architecture:** Keep perception, reasoning, decision-making, and actuation independently extensible.
- **Resource awareness:** Consider hardware, compute, latency, and connectivity constraints.
- **Open research:** Share code, documentation, and reproducible experiments.

## Long-Term Vision

The long-term objective is to develop a modular embodied intelligence architecture capable of operating across different physical robotic platforms.

Potential future capabilities include:

- Real-time visual perception.
- Context-aware physical behaviour.
- Autonomous navigation and interaction.
- Persistent episodic memory.
- Adaptive decision-making.
- Local and cloud AI coordination.
- Uncertainty-aware behaviour.
- Learning from physical experience.
- Resilient operation under limited resources.

These are research directions, not currently completed capabilities.

## Open Research

Cozmo Reborn is an evolving experimental project.

The intention is to investigate the possibilities and limitations of intelligent behaviour on accessible, resource-constrained robotic hardware, while documenting the engineering process transparently.

**The goal is not simply to make an old robot smarter. It is to explore how intelligence can emerge through the interaction of perception, reasoning, memory, action, and physical experience.**

---

**Project:** Cozmo Reborn  
**Research Focus:** Resource-Aware Embodied Intelligence  
**Platform:** Original Anki Cozmo  
**Development:** Open Source
