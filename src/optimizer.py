"""
optimizer.py

This module implements the optimization logic to improve robotic arm motion 
through gradient descent.

Core Responsibilities:
- Define the cost function based on distance to target and energy efficiency.
- Compute gradients of the cost function with respect to joint angles.
- Apply manual gradient descent to optimize joint angles iteratively.

Author(s): Verónica Elze, Sumit Chahar, Rosalia Miray
Course: DS623 Math & Statistics for Data Science
Institution: City University of Seattle
"""

# Import necessary libraries
import numpy as np
from math import sqrt
from src.robotic_arm import forward_kinematics  # Adjust path if needed

# Define cost function
def compute_cost(theta1, theta2, target_x, target_y, link1_length=1.0, link2_length=1.0):
    """
    Compute the cost as the Euclidean distance between end-effector and target.

    Parameters:
    - theta1, theta2: joint angles (radians)
    - target_x, target_y: target coordinates
    - link1_length, link2_length: lengths of the two arm segments

    Returns:
    - cost: Euclidean distance to target
    """
    x, y = forward_kinematics(theta1, theta2, link1_length, link2_length)
    cost = sqrt((x - target_x)**2 + (y - target_y)**2)
    return cost

# Define gradient computation
def compute_gradients(theta1, theta2, target_x, target_y, epsilon=1e-5, link1_length=1.0, link2_length=1.0):
    """
    Compute numerical gradients of the cost function with respect to theta1 and theta2 using finite differences.

    Parameters:
    - theta1, theta2: Current joint angles (radians)
    - target_x, target_y: Target coordinates
    - epsilon: Small perturbation value for finite difference

    Returns:
    - grad_theta1, grad_theta2: Estimated gradients
    """
    cost = compute_cost(theta1, theta2, target_x, target_y, link1_length, link2_length)

    cost_theta1 = compute_cost(theta1 + epsilon, theta2, target_x, target_y, link1_length, link2_length)
    grad_theta1 = (cost_theta1 - cost) / epsilon

    cost_theta2 = compute_cost(theta1, theta2 + epsilon, target_x, target_y, link1_length, link2_length)
    grad_theta2 = (cost_theta2 - cost) / epsilon

    return grad_theta1, grad_theta2

# Define gradient descent optimizer
def optimize_arm(initial_theta1, initial_theta2, target_x, target_y, learning_rate=0.1, iterations=100, verbose=True, link1_length=1.0, link2_length=1.0):
    """
    Perform gradient descent to optimize joint angles.

    Parameters:
    - initial_theta1, initial_theta2: starting joint angles (radians)
    - target_x, target_y: coordinates of the target point
    - learning_rate: step size for updates
    - iterations: number of iterations to run

    Returns:
    - optimized_theta1, optimized_theta2: final joint angles (radians)
    - history: list of (theta1, theta2, cost) tuples over iterations
    """
    theta1, theta2 = initial_theta1, initial_theta2
    history = []

    for i in range(iterations):
        cost = compute_cost(theta1, theta2, target_x, target_y, link1_length, link2_length)
        grad1, grad2 = compute_gradients(theta1, theta2, target_x, target_y)

        theta1 -= learning_rate * grad1
        theta2 -= learning_rate * grad2

        history.append((theta1, theta2, cost))

        if verbose and (i % 10 == 0 or i == iterations - 1):
            print(f"Iteration {i+1}: Cost = {cost:.4f}")

    return theta1, theta2, history

# OpenAI. (2025). ChatGPT’s assistance with mathematical modeling and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt