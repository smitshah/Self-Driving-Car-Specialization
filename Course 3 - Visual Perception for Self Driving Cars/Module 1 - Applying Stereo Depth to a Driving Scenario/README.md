# Practice Assignment: Applying Stereo Depth to a Driving Scenario

For this practice notebook, you will use what you've learned in the past Module to locate a car in a scene and estimate how far you are from it using a stereo camera model. This exercise gives you a brief introduction to using Python to implement what you've recently learned in order to find the distance to collision with an obstacle.

After this assignment you will be able to:
* Use OpenCV to complete standard vision tasks.
* Understand the process of obtaining depth from a pair of stereo images and their respective projection matrices.
* Understand the advantages of cross-correlation for localization of important information in an image.

# Practice Programming Assignment: (Submission) Applying Stereo Depth to a Driving Scenario

After finishing the Jupyter notebook for this assessment, please fill in the provided output.yaml file according to the output of the last section. Submit the output.yaml file only.

[output.yaml]( https://d3c33hcgiwev3.cloudfront.net/hQr2kBUXEemYdRIT0BhLtg_85333eb0151711e9b758fd32c0f01c89_output.yaml?Expires=1589328000&Signature=ZKiY6ZLNHAp5ZKYskxJ0MwJgIACxccaKWNTtUcO42zZLd42L~As7PWS2sNdBnlZBK8tM0gNF6gX9kqBoHT5iS1mJl7l4MPATEOXlClB5p7DoDfbsNxZUIWsAyK4T-b5nEfpukQBSmw-l3r~P6J6ZN3sEqmcgVZV~gf1NnAMzHY4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

| **Task** | **Grade** | **Grading Criterion** |
| --------------- | --------------- | --------------- |
| Decompose Projection Matrices | 30% | A full mark is awarded if the projection matrices elements are within a tolerance of 0.01 from the ground truth ones. |
| Obstacle Location Estimation | 35% | A full mark is awarded if the estimated coordinates are within a tolerance of 0.01 from the correct obstacle coordinates. |
| Closest Point Depth Estimation | 35% | A full mark is awarded if the estimated closest point depth is within a tolerance of 0.05 from the ground truth depth. |

