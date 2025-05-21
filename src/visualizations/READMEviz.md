# /src/visualizations

This folder contains modular, reusable scripts for generating visual outputs from the Optimotion simulation.

## Contents:
- `cost_convergence_plot.py` – Plots cost vs. iteration to evaluate optimization behavior
- `pose_comparison_plot.py` – Compares initial and optimized arm poses side-by-side
- `fwd_kinematics_plot.py` – Plots a static arm pose from a given joint configuration

## Notes:
- All functions accept `output_dir` and `filename` as parameters for consistent path control
- Plots are used in TP02 Methodology and Appendix B
- Output files are saved to `/outputs/` and referenced from `run_poc_sim.ipynb`

## Acknowledgments
OpenAI. (2025). *ChatGPT’s assistance with mathematical modeling and code generation for DS623 Optimotion project* [Large language model]. https://openai.com/chatgpt
