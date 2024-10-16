# AutonomousRoboticVehicle

This repository contains the code for an AI-based **Autonomous Vehicle System** that focuses on self-driving capabilities, scene understanding, and intelligent navigation. The project integrates multiple sensors, computer vision techniques, and machine learning algorithms to allow the vehicle to understand its environment, make real-time decisions, and navigate autonomously. 

## Project Overview

The goal of this project is to develop an autonomous vehicle system capable of scene understanding, path planning, and real-time decision-making. The system uses several modules to process environmental data, analyze scenes using AI, and control the vehicle's movement.

### Key Features:
- **Sensor Integration**: Uses cameras, LiDAR (if applicable), and ultrasonic sensors to gather environmental data.
- **Scene Understanding**: AI-based scene analysis to detect objects, lanes, and other vehicles, allowing the system to understand the driving environment.
- **Computer Vision**: Object detection, lane detection, and other image processing tasks using state-of-the-art computer vision algorithms.
- **Decision Making**: A Finite State Machine (FSM) is used to manage real-time decisions, including lane following, obstacle avoidance, and overtaking.
- **Path Planning**: Integration with Google Maps API for dynamic route planning and local path planning to avoid obstacles.
- **Control System**: Real-time control of the vehicle's steering, acceleration, and braking based on input from decision and planning modules.

## Code Structure

### 1. **Perception Module** (`/perception`)
   This module includes code for sensor integration, data collection, and computer vision tasks, such as object detection, lane detection, and environmental perception.

### 2. **Scene Understanding Module** (`/scene_understanding`)
   This folder contains AI models and algorithms used for scene understanding, which helps the vehicle recognize objects, interpret the driving environment, and make decisions based on visual inputs.

### 3. **Decision-Making Module** (`/decision_making`)
   Contains the FSM logic and decision-making algorithms for handling various driving scenarios, such as lane following, overtaking, and obstacle avoidance.

### 4. **Path Planning Module** (`/path_planning`)
   This folder includes code for dynamic path planning using the Google Maps API, as well as local path adjustments to avoid obstacles.

### 5. **Control Module** (`/control`)
   The control module translates the decisions from the FSM into vehicle actions such as steering, accelerating, or braking.

## Prerequisites

To run this code, the following dependencies are required:
- Python 3.x
- OpenCV (for computer vision)
- TensorFlow (for AI models)
- Google Maps API key
- Other relevant libraries for sensor and data processing

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/zainbam/AutonomousRoboticVehicle.git
   cd AutonomousRoboticVehicle
