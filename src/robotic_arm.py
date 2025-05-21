"""
robotic_arm.py

This module defines the mathematical structure and behavior of a simple 2D robotic arm.

Core Responsibilities:
- Implement forward kinematics for a two-joint planar robotic arm.
- Calculate the end-effector position based on joint angles.
- Define helper functions for arm visualization (optional).

Author(s): Verónica Elze, Sumit Chahar, Rosalia Miray
Course: DS623 Math & Statistics for Data Science
Institution: City University of Seattle
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define forward kinematics function
def forward_kinematics(theta1, theta2, link1_length=1.0, link2_length=1.0):
    """
    Calculate end-effector (x, y) position given two joint angles.

    Parameters:
    - theta1: Angle of first joint (radians)
    - theta2: Angle of second joint (radians)
    - link1_length: Length of first arm segment
    - link2_length: Length of second arm segment

     Returns:
    - Tuple: (x, y) coordinates of the end-effector
    """
    x = link1_length * np.cos(theta1) + link2_length * np.cos(theta1 + theta2)
    y = link1_length * np.sin(theta1) + link2_length * np.sin(theta1 + theta2)
    return x, y

# === Example test case ===
if __name__ == "__main__":
    # Test case: both joint angles are 0 radians
    theta1 = np.radians(0)
    theta2 = np.radians(0)
    x, y = forward_kinematics(theta1, theta2)
    print(f"End-effector position for θ1=0°, θ2=0°: ({x:.2f}, {y:.2f})")
    
# OpenAI. (2025). ChatGPT’s assistance with mathematical modeling and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt