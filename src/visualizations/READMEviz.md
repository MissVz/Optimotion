# /src/visualizations

This folder contains scripts responsible for generating static and dynamic visualizations from simulation outputs.

## Intended Contents:
- Static plots of robotic arm trajectories
- Cost function convergence graphs
- Animated motion trajectory (if stretch goal achieved)

## Example Future Files:
- `plot_trajectory.py`
- `plot_cost_function.py`
- `animate_arm_movement.py`

## Notes:
- Visualizations use `matplotlib` (and optionally `matplotlib.animation` for dynamic plots).
- Outputs from these scripts should be saved to the `/outputs` directory.
- Scripts should be modular and accept inputs (e.g., joint angles, costs) rather than hardcoding data.

---
