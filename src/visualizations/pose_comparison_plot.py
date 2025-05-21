# pose_comparison_plot.py

import matplotlib.pyplot as plt
import numpy as np
import os
from src.robotic_arm import forward_kinematics  # ✅ Import the true source

def plot_pose_comparison(theta1_init, theta2_init, theta1_opt, theta2_opt, title="Pose Comparison: Initial vs. Optimized", output_dir="outputs", filename="pose_comparison_initial_vs_optimized.png"):
    """
    Plot side-by-side comparison of initial and optimized arm configurations.
    """
    x0, y0 = 0, 0

    x1i = np.cos(theta1_init)
    y1i = np.sin(theta1_init)
    x2i, y2i = forward_kinematics(theta1_init, theta2_init)

    x1o = np.cos(theta1_opt)
    y1o = np.sin(theta1_opt)
    x2o, y2o = forward_kinematics(theta1_opt, theta2_opt)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    for i, (x1, y1, x2, y2, label) in enumerate([
        (x1i, y1i, x2i, y2i, "Initial Pose"),
        (x1o, y1o, x2o, y2o, "Optimized Pose")
    ]):
        ax[i].plot([x0, x1], [y0, y1], 'bo-', label='Link 1')
        ax[i].plot([x1, x2], [y1, y2], 'ro-', label='Link 2')
        ax[i].scatter([x2], [y2], color='green', label='End Effector', zorder=5)
        ax[i].set_xlim(-2, 2)
        ax[i].set_ylim(-2, 2)
        ax[i].set_aspect('equal')
        ax[i].set_title(label)
        ax[i].grid(True)
        ax[i].legend()

    fig.suptitle(title)
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)
    
    plt.savefig(output_path)
    print(f"✅ Pose comparison plot saved to: {output_path}")
    plt.show()

# OpenAI. (2025). ChatGPT’s assistance with ploting and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt