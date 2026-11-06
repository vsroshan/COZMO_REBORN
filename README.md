# 🤖 Cozmo Reborn

### Open Research in Resource-Aware Embodied Intelligence

**Cozmo Reborn** is an independent open-source research and engineering project exploring how modern AI architectures can enable intelligent physical behaviour on resource-constrained and legacy robotic platforms.

Using the original Anki Cozmo as its initial experimental platform, the project investigates the intersection of Physical AI, embodied intelligence, edge computing, computer vision, autonomous decision-making and robotics.

Rather than building another conversational robot, the objective is to investigate the underlying intelligence that enables physical systems to perceive their surroundings, reason about possible actions, execute decisions, evaluate outcomes and adapt to changing environments.

## Research Question

**How can resource-constrained robotic systems achieve reliable, adaptive and context-aware physical behaviour through modular, open-source AI architectures?**

## Research Objectives

1. **Resource-Aware Intelligence:** Investigate how AI workloads can be distributed between embedded hardware and external computing resources.
2. **Closed-Loop Reasoning:** Explore perception-action-feedback architectures that evaluate the physical consequences of robot actions.
3. **Uncertainty-Aware Autonomy:** Investigate decision-making under incomplete observations and uncertain environmental conditions.
4. **Experience-Based Adaptation:** Explore memory, feedback and learning mechanisms that improve subsequent robot decisions.
5. **Hardware-Agnostic Intelligence:** Develop modular software components that can eventually be adapted across multiple robotic embodiments.

## Initial Experimental Platform

The project begins with the original Anki Cozmo, a compact consumer robot featuring a camera, display, motors and onboard sensors.

A Raspberry Pi 3 is the proposed embedded computing platform, with a MacBook Pro initially serving as the development and experimentation environment.
##  Current Status

**Initiated: 3 November 2026**

Currently beginning with hardware verification, SDK exploration, and establishing the development environment.

## Core Research Areas

- Physical AI and embodied intelligence
- Edge AI and resource-constrained inference
- Vision-language-action architectures
- Sensorimotor feedback systems
- World models and predictive reasoning
- Autonomous decision-making
- Uncertainty estimation and failure recovery
- Modular robotics software
- Multi-platform embodied intelligence

## Development Philosophy

The project follows an experiment-driven, open-source development approach.

Architectural decisions, experiments, observations, limitations and evaluation results will be documented transparently.

The objective is to develop reproducible experiments and investigate meaningful engineering and research questions rather than simply integrate existing AI services into a robotic platform.

## Long-Term Vision

Cozmo Reborn aims to evolve into a modular experimental framework for investigating embodied intelligence across different physical systems.

The initial focus is a single robot. Future exploration may extend to other robotic platforms, including aerial robotics, to investigate how common intelligence architectures can adapt to different physical embodiments.

**The central idea: Intelligence should not stop at understanding the world. It should be able to interact with it, observe the consequences and adapt.**
## Development Log

### Experiment 001 — First Hardware Connection

**Status:** Completed  
**Date:** 4 November 2026

**Objective:** Establish a direct connection between the original Anki Cozmo robot and a Python-based control system using an independent, open-source library.

**Hardware and software:**
- Original Anki Cozmo robot
- MacBook Pro
- Python 3.11
- PyCozmo (third-party Python library)

**Implementation:**

Created and executed `first_connection.py` to establish a connection with Cozmo and send physical movement commands.

The experiment:
1. Established a connection with the robot.
2. Sent a command to raise Cozmo's head.
3. Sent a second command to return its head to the neutral position.

**Result:** Successful. Cozmo physically moved its head in response to both commands.

**Research significance:**

This establishes the first working communication and control pathway between the development environment and the physical robot. It provides the foundation for future perception, closed-loop reasoning and embodied intelligence experiments.

### Experiment 002 — Camera Capture

**Status:** Completed (update after successful test)  
**Date:** 6 November 2026

**Objective:** Establish access to the original Anki Cozmo's onboard camera using an independent Python-based communication library.

**Hardware and software:**
- Original Anki Cozmo robot
- MacBook Pro
- Python 3.11
- PyCozmo
- Wi-Fi direct communication

**Implementation:**

Created `camera_capture.py` to:
1. Establish a direct connection with Cozmo.
2. Enable its onboard colour camera.
3. Receive a camera image through PyCozmo's camera event handler.
4. Save the captured image locally as `camera_capture.png`.

**Expected output:** A locally saved image captured directly from Cozmo's onboard camera.
<img width="320" height="240" alt="camera_capture" src="https://github.com/user-attachments/assets/eb27a6e0-203e-4dd7-9fda-fb7c1c166ba3" />


**Research significance:**

This experiment investigates the visual perception capabilities of legacy robotic hardware through an independent open-source software stack.

Successful camera access establishes an initial foundation for computer vision, environmental perception and future perception-action experiments.

**Next experiment:** Experiment 003 — Computer Vision and Object Detection using OpenCV.
