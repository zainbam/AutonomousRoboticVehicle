# Perception Module

This folder contains the code for the **Perception Module** of the autonomous vehicle system. The module uses the **Intel RealSense Depth Camera D455** for stereo vision and object distance measurement.

## Features

1. **Stereo Vision Calibration**:
   - The calibration files provided in this folder use the **triangulation method** to configure the stereo camera setup, enabling accurate depth information capture.

2. **Object Distance Calculation**:
   - This module includes code that calculates the distance to detected objects. You can pass the bounding box coordinates of the object in an array, and the system will compute the distance with around **90% accuracy** for objects up to **10 meters** away.

## Requirements

- **Intel RealSense SDK**
- **OpenCV**

## How to Use

1. Connect the **Intel RealSense Depth Camera D455**.
2. Run the calibration file to set up the stereo vision system.
3. Use the distance calculation code to pass object bounding box coordinates and compute distances.

