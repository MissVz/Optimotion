import matplotlib.pyplot as plt
import os

def plot_cost_convergence(cost_values, title="Cost Convergence Over Iterations", output_dir="outputs", filename="cost_convergence_plot.png"):
    """
    Plot cost function convergence over iterations and save it.

    Parameters:
    - cost_values: List of cost values
    - title: Title of the plot
    - filename: Output filename to save the plot
    """
    iterations = len(cost_values)
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, iterations + 1), cost_values, marker='o', color='darkorange')
    plt.title(title)
    plt.xlabel("Iteration")
    plt.ylabel("Cost")
    plt.grid(True)
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    plt.savefig(output_path)
    print(f"✅ Cost convergence plot saved to: {output_path}")
    plt.show()