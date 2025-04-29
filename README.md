Optimotion: Gradient-Based Robotic Arm Optimization
City University of Seattle – DS623 Math & Statistics for Data Science

Team Members:
Verónica Elze (Master of Artificial Intelligence)
Sumit Chahar (Master of Data Science)
Rosalia Miray (Master of Data Science)

Project Overview:
Optimotion simulates and optimizes a two-joint robotic arm using foundational mathematical principles.
We manually implement forward kinematics, cost function design, and gradient descent using NumPy and Pandas to achieve energy-efficient, goal-oriented robotic movement.
Visualizations are generated with Matplotlib to illustrate optimization progress and movement paths.

Stretch goals include creating animated simulations of the robotic arm's trajectory improvements.

This project applies:
Linear algebra (matrices, vectors)
Vector calculus (gradients, partial derivatives)
Numerical optimization techniques (gradient descent)
Data visualization and analysis

Project Structure:
/docs               # Deliverables: TP01, TP02, TP03, team charter, references
/src
    /data           # Generated joint angle configurations (if needed)
    /visualizations # Scripts for plotting trajectories, cost function behavior
    robotic_arm.py  # Forward kinematics and arm modeling
    optimizer.py    # Cost function, gradient calculations, optimization steps
/tests              # Unit tests and validation scripts (optional)
/outputs            # Plots, convergence graphs, animation outputs
/notebooks          # Jupyter notebooks for early experiments and demos
/config             # (Optional) Configuration files for parameters
README.md
.gitignore

Key Concepts:
Forward Kinematics: Calculating end-effector positions based on joint angles.
Cost Function Minimization: Designing a function that penalizes long paths and high energy usage.
Gradient Descent: Manually calculating gradients to iteratively optimize movement.
Visualization: Plotting convergence behavior, motion paths, and potential animated demonstrations.

Technologies Used:
Python 3.11+
NumPy
Pandas
Matplotlib
Jupyter Notebook

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
2. (Optional) Set up a Python virtual environment:
bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
3. Run initial kinematic simulations:
bash
python src/robotic_arm.py
4. Run optimization:
bash
python src/optimizer.py
5. View outputs in /outputs folder (plots, visualizations).


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

License
This project is intended for educational and research purposes as part of DS623 – City University of Seattle.

Team Optimotion – Powered by Math, Movement, and Mastery