
"""
test_robotic_arm.py

This test script includes unit tests to verify the correctness of core functions
used in the Optimotion project PoC, specifically forward kinematics and the cost function.

Student: Verónica Elze
Course: DS623 Math & Statistics for Data Science
"""

# Import necessary libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import necessary modules
from src.robotic_arm import forward_kinematics
from src.optimizer import compute_cost

# Test cases for the robotic arm's forward kinematics and cost function
def test_forward_kinematics_zero_angles():
    """
    Test that the end-effector reaches (2.0, 0.0) when both joint angles are 0.
    This validates basic forward kinematics when the arm is fully extended.
    """
    theta1 = 0 # Joint angle 1
    theta2 = 0 # Joint angle 2
    
    # Compute the end-effector position using forward kinematics
    x, y = forward_kinematics(theta1, theta2)
    
    # Check if the end-effector position is as expected
    # The expected position is (2.0, 0.0) when both angles are 0
    assert round(x, 5) == 2.0
    assert round(y, 5) == 0.0
    
    # Print the end-effector position for debugging purposes
    print(f"End-effector position: x={x}, y={y}")
    
    # This message indicates that the test has passed successfully
    print("✅ test_forward_kinematics_zero_angles passed.")

# Test cases for the cost function
def test_cost_at_target():
    """
    Test that the cost is zero when the end-effector exactly reaches the target.
    Validates correctness of the compute_cost function.
    """
    theta1 = 0 # Joint angle 1
    theta2 = 0 # Joint angle 2
    
    # Target position for the end-effector
    target_x, target_y = 2.0, 0.0
    
    # Compute the cost at the target position
    cost = compute_cost(theta1, theta2, target_x, target_y)
    assert round(cost, 5) == 0.0 # Cost should be zero at the target
    
    # Print the cost for debugging purposes
    print(f"Cost at target: {cost}")
    
    # This message indicates that the test has passed successfully
    print("✅ test_cost_at_target passed.")

# Run the tests
# This block ensures that the tests are executed when the script is run directly.
if __name__ == "__main__":
    test_forward_kinematics_zero_angles()
    test_cost_at_target()

# OpenAI. (2025). ChatGPT’s assistance with code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt