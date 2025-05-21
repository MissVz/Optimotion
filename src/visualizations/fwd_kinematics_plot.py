# forward_kinematics_plot.py

import matplotlib.pyplot as plt
import numpy as np
import os
from src.robotic_arm import forward_kinematics

def plot_robot_arm(theta1, theta2, link1_length=1.0, link2_length=1.0, title=""):
    x0, y0 = 0, 0
    x1 = link1_length * np.cos(theta1)
    y1 = link1_length * np.sin(theta1)
    x2, y2 = forward_kinematics(theta1, theta2, link1_length, link2_length)

    plt.figure(figsize=(6, 6))
    plt.plot([x0, x1], [y0, y1], 'bo-', label='Link 1')
    plt.plot([x1, x2], [y1, y2], 'ro-', label='Link 2')
    plt.scatter([x2], [y2], color='green', label='End Effector', zorder=5)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.gca().set_aspect('equal')
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "trajectory_plot_sample.png")
    plt.savefig(output_path)
    print(f"✅ Trajectory plot saved to: {output_path}")
    plt.show()
    
# OpenAI. (2025). ChatGPT’s assistance with ploting and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt