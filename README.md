Optimotion: Gradient-Based Robotic Arm Optimization
City University of Seattle – DS623 Math & Statistics for Data Science

Team Members:
Verónica Elze (Master of Artificial Intelligence)

Project Overview:
Optimotion simulates and optimizes a two-joint robotic arm using foundational mathematical principles.
We manually implement forward kinematics, a cost function, and gradient descent using NumPy and Matplotlib to optimize motion toward a target position.
A fully functional Proof of Concept (PoC) includes an end-to-end notebook simulation, cost convergence analysis, and pose visualization plots.

Stretch goals include trajectory animation and exploration of parameter sensitivity.

Phase II:   PoC phase of the project only simulates and optimizes a 2-joint robotic arm using gradient descent. 
            The PoC implementation includes a complete optimization loop, visual validation, and TP02-ready documentation.

This project applies:
Linear algebra (matrices, vectors)
Vector calculus (gradients, partial derivatives)
Numerical optimization techniques (gradient descent)
Data visualization and analysis

Project File Structure:
/config
    READMEcfg.md           # Placeholder for future configuration files
/docs
    REFERENCES.md          # APA-formatted references for TP01 & TP02
/notebooks
    run_poc_sim.ipynb      # Complete PoC notebook for TP02 Appendix B
    run_poc_sim.html/pdf   # Exports of the notebook for TP02 submission
    READMEnb.md            # Notebook folder overview
/outputs
    poc_cost_convergence.png       # Line plot of cost function values across optimization iterations
    poc_pose_comparison.png        # Side-by-side plot of initial and optimized robotic arm configurations
    run_poc_sim.html/pdf   # Output copy for portability
    READMEouts.md          # Description of plots and simulation results
/src
    /data
        READMEdata.md      # Notes: no persistent datasets used in TP02
    /visualizations
        cost_convergence_plot.py     # Plots cost vs. iteration to show optimization progress
        fwd_kinematics_plot.py       # Visualizes a single arm pose from joint angles
        pose_comparison_plot.py      # Compares initial vs. optimized arm configurations
        READMEviz.md       # Overview of plot script responsibilities
    optimizer.py           # Cost, gradients, and optimization loop
    robotic_arm.py         # Forward kinematics calculation
/tests
    test_robotic_arm.py    # Unit test for FK (extendable)
/.gitignore
requirements.txt
README.md

Key Concepts:
Forward Kinematics: Calculating end-effector positions based on joint angles.
Cost Function Minimization: Designing a function that penalizes long paths and high energy usage.
Gradient Descent: Manually calculating gradients to iteratively optimize movement.
Visualization: Plotting convergence behavior, motion paths, and potential animated demonstrations.

Technologies Used:
Python 3.11+
NumPy
Pandas (to be implemented in future phase)
Matplotlib
Jupyter Notebook
ipykernel

Project Timeline & Milestones:
Phase	        Milestones
TP01 Proposal	✅ Completed (April 2025)
TP02 Progress Report	⏳ In Progress (due May 25, 2025)
TP03 Final Report	Planned (June 2025)
TP04 Presentation	Planned (June 2025)

How to Run:
1. Clone this repository:
bash
git clone https://github.com/yourusername/Optimotion-DS623.git
cd Optimotion-DS623
2. Run Jupyter Notebook notebooks/run_poc_sim.ipynb
3. View /outputs folder for plots and visualizations


MLOps Light Practices:
Clear folder structure
Version-controlled simulation scripts
Modular and reusable code (/src)
Output separation (/outputs)
Experimentation space (/notebooks)
Clean documentation (/docs)

References:
See /docs/REFERENCES.md for full academic citations, including:
OpenAI Gym
DeepMind Control Suite
Craig's Introduction to Robotics: Mechanics and Control
Other academic sources used in TP01/TP02/TP03

Acknowledgments:
This project benefited from generative support provided by:
OpenAI. (2025). *ChatGPT’s assistance with mathematical modeling and code generation for DS623 Optimotion project* [Large language model]. https://openai.com/chatgpt

License
This project is intended for educational and research purposes as part of DS623 – City University of Seattle.

Team Optimotion – Powered by Math, Movement, and Mastery