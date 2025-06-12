
"""
optimizer.py

This module implements the optimization logic to improve robotic arm motion 
through gradient descent, including advanced techniques like learning rate decay,
regularization penalties, and convergence thresholding.

Core Responsibilities:
- Define the cost function with optional penalty terms
- Compute gradients of the cost function with respect to joint angles
- Apply gradient descent using configurable optimization strategies

Author(s): Verónica Elze, Sumit Chahar, Rosalia Miray
Course: DS623 Math & Statistics for Data Science
Institution: City University of Seattle
"""

# Import necessary libraries
import numpy as np
from math import sqrt
from src.robotic_arm import forward_kinematics  # Adjust path if needed

def compute_cost(theta1, theta2, target_x, target_y, 
                 link1_length=1.0, link2_length=1.0, 
                 lambda_energy=0.0, lambda_smooth=0.0,
                 prev_theta1=None, prev_theta2=None):
    """
    Compute the cost as the Euclidean distance between end-effector and target,
    with optional penalties for energy (large angles) and sudden angle changes.

    Parameters:
    - theta1, theta2: joint angles (radians)
    - target_x, target_y: target coordinates
    - link1_length, link2_length: lengths of the arm segments
    - lambda_energy: penalty coefficient for energy (angle magnitude)
    - lambda_smooth: penalty for sudden angle changes
    - prev_theta1, prev_theta2: previous angles to penalize movement change

    Returns:
    - total cost: distance + regularization penalties
    """
    x, y = forward_kinematics(theta1, theta2, link1_length, link2_length)
    # Distance to target (main cost)
    distance_cost = np.sqrt((x - target_x) ** 2 + (y - target_y) ** 2)

    # Technique: Energy Penalty (Regularization)
    # Penalizes large joint angles to promote energy-efficient poses
    energy_penalty = lambda_energy * (theta1 ** 2 + theta2 ** 2)

    # Technique: Angle Change Penalty (Smoothness Regularization)
    # Penalizes drastic changes from previous angles to promote smoother movement
    smooth_penalty = 0
    if prev_theta1 is not None and prev_theta2 is not None:
        smooth_penalty = lambda_smooth * ((theta1 - prev_theta1) ** 2 + (theta2 - prev_theta2) ** 2)

    return distance_cost + energy_penalty + smooth_penalty

def compute_gradients(theta1, theta2, target_x, target_y,
                      link1_length, link2_length,
                      lambda_energy, lambda_smooth,
                      prev_theta1, prev_theta2,
                      delta=1e-6):
    """
    Compute numerical gradients of the cost function with respect to theta1 and theta2 using finite differences.

    Parameters:
    - theta1, theta2: Current joint angles (radians)
    - target_x, target_y: Target coordinates
    - epsilon: Small perturbation value for finite difference

    Returns:
    - grad_theta1, grad_theta2: Estimated gradients
    """
    cost_plus = compute_cost(theta1 + delta, theta2, target_x, target_y,
                             link1_length, link2_length,
                             lambda_energy, lambda_smooth,
                             prev_theta1, prev_theta2)

    cost_minus = compute_cost(theta1 - delta, theta2, target_x, target_y,
                              link1_length, link2_length,
                              lambda_energy, lambda_smooth,
                              prev_theta1, prev_theta2)

    grad_theta1 = (cost_plus - cost_minus) / (2 * delta)

    cost_plus = compute_cost(theta1, theta2 + delta, target_x, target_y,
                             link1_length, link2_length,
                             lambda_energy, lambda_smooth,
                             prev_theta1, prev_theta2)

    cost_minus = compute_cost(theta1, theta2 - delta, target_x, target_y,
                              link1_length, link2_length,
                              lambda_energy, lambda_smooth,
                              prev_theta1, prev_theta2)

    grad_theta2 = (cost_plus - cost_minus) / (2 * delta)

    return grad_theta1, grad_theta2

def optimize_arm(theta1_init, theta2_init, target_x, target_y,
                 learning_rate=0.1, iterations=100, link1_length=1.0, link2_length=1.0,
                 lambda_energy=0.0, lambda_smooth=0.0, decay_rate=0.0, epsilon=1e-5,
                 verbose=False):
    """
    Perform gradient descent to optimize joint angles.

    Parameters:
    - theta1_init, theta2_init: initial guess of angles (radians)
    - target_x, target_y: target position for end-effector
    - learning_rate: step size for gradient update
    - iterations: maximum number of iterations
    - lambda_energy: coefficient for energy penalty term
    - lambda_smooth: coefficient for smoothness penalty
    - decay_rate: rate at which learning rate decays over time
    - epsilon: convergence threshold for cost difference
    - verbose: print progress if True

    Returns:
    - optimized_theta1, optimized_theta2: final joint angles (radians)
    - history: list of (theta1, theta2, cost) tuples over iterations
    """
    theta1, theta2 = theta1_init, theta2_init
    prev_theta1, prev_theta2 = theta1_init, theta2_init
    history = []
    prev_cost = float('inf')

    for i in range(iterations):
        # Apply learning rate decay
        lr = learning_rate / (1 + decay_rate * i)

        # Modular gradient computation
        grad_theta1, grad_theta2 = compute_gradients(theta1, theta2, target_x, target_y,
                                                     link1_length, link2_length,
                                                     lambda_energy, lambda_smooth,
                                                     prev_theta1, prev_theta2)

        # Update joint angles
        theta1 -= lr * grad_theta1
        theta2 -= lr * grad_theta2

        # Compute current cost
        cost = compute_cost(theta1, theta2, target_x, target_y,
                            link1_length, link2_length,
                            lambda_energy, lambda_smooth,
                            prev_theta1, prev_theta2)

        history.append((theta1, theta2, cost))

        if verbose:
            print(f"Iter {i+1}: cost = {cost:.6f}, θ1 = {np.degrees(theta1):.2f}, θ2 = {np.degrees(theta2):.2f}")

        # Early stop based on convergence threshold
        if abs(prev_cost - cost) < epsilon:
            if verbose:
                print(f"Converged at iteration {i+1}")
            break

        prev_cost = cost
        prev_theta1, prev_theta2 = theta1, theta2

    return theta1, theta2, history

# OpenAI. (2025). ChatGPT’s assistance with mathematical modeling and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt