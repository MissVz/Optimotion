import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def plot_cost_contour_from_history(history, title="Cost landscape Over Iterations", output_dir="outputs", filename="cost_landscape_contour.png"):
    # Extract theta1, theta2, and cost from history
    theta1 = np.array([h[0] for h in history])
    theta2 = np.array([h[1] for h in history])
    cost = np.array([h[2] for h in history])

    # Create a grid for contour plotting
    grid_x, grid_y = np.mgrid[
        theta1.min():theta1.max():100j,
        theta2.min():theta2.max():100j
    ]
    grid_cost = griddata(
        (theta1, theta2), cost, (grid_x, grid_y), method='cubic'
    )

    # Plot contour
    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contourf(grid_x, grid_y, grid_cost, levels=50, cmap='viridis')
    ax.plot(theta1, theta2, color='r', marker='o', label='Optimizer Path')
    ax.set_xlabel(r'$\theta_1$ (rad)')
    ax.set_ylabel(r'$\theta_2$ (rad)')
    ax.set_title(title)
    fig.colorbar(contour)
    ax.legend()
    plt.tight_layout()
    plt.savefig(f"{output_dir}/{filename}")
    plt.show()
    print(f"✅ Cost landscape contour plot saved to: {output_dir}/{filename}")

# OpenAI. (2025). ChatGPT’s assistance with ploting and code generation for DS623 Optimotion project [Large language model]. https://openai.com/chatgpt