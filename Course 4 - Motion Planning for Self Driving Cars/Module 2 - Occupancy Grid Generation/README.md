# Occupancy Grid Generation

Welcome to the assignment for Module 2: Mapping for Planning. In this assignment, you will be generating an occupancy grid using LIDAR scanner measurements from a moving vehicle in an unknown environment. You will use the inverse scanner measurement model developed in the lessons to map these measurements into occupancy probabilities, and then perform iterative log-odds updates to an occupancy grid belief map. After the car has gathered enough data, your occupancy grid should converge to the true map.

**In this assignment, you will:**
* Gather range measurements of a moving car's surroundings using a lidar scanning function.
* Extract occupancy information from the range measurements using an inverse scanner model.
* Perform logodds updates on an occupancy grids based on incoming measurements.
* Iteratively construct a probabilistic occupancy grid from those log odds updates.

For most exercises, you are provided with a suggested outline. You are encouraged to diverge from the outline if you think there is a better, more efficient way to solve a problem.

# Programming Assignment: (Submission) 

After finishing the Jupyter notebook for this assessment, please save your output in “occ_grid_values.txt” format only.
