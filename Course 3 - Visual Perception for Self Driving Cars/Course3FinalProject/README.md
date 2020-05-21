# Environment Perception For Self-Driving Cars

Welcome to the final assignment in this course. In this assignment, you will learn how to use the material so far to extract useful scene information to allow self-driving cars to safely and reliably traverse their environment.

**In this assignment, you will:**
* Use the output of semantic segmentation neural networks to implement drivable space estimation in 3D.
* Use the output of semantic segmentation neural networks to implement lane estimation.
* Use the output of semantic segmentation to filter errors in the output of 2D object detectors.
* Use the filtered 2D object detection results to determine how far obstacles are from the self-driving car.

Launch the Jupyter Notebook to begin!

# Programming Assignment: (Submission) Environment Perception For Self-Driving Cars

**Submission:**

After finishing the Jupyter notebook for this assessment, please fill in the provided output.yaml file according to the output of the last section. Submit the output.yaml file only.

[output.yaml]( https://d3c33hcgiwev3.cloudfront.net/hfIJ8Oj6Eei5Kg7DUflKxA_866f28a0e8fa11e89d12158c8557aff5_output.yaml?Expires=1590192000&Signature=US4iTLqzyQWe7yS9ahVFbOhsv~2w4U1Fu6XwxkosJ7i~sKYHhMAv0~QbTNBZXwne78ptF94AeVyr9VqOorlBXqe27N66dyGuLLnhlM~rnQ46~o-P7gzfCQQgJH~g8cbnKdpvY0Wr6z1PF97vNo8Mog~02lt3F3xpyBD4iEGQXLE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

As an example, you will need to copy the highlighted output of the notebook seen bellow,

![img1](https://user-images.githubusercontent.com/42312238/82579397-5ec67a00-9bab-11ea-9a88-a3655a85a899.png)

to the corresponding highlighted space in the output.yaml file:

![img2](https://user-images.githubusercontent.com/42312238/82579421-67b74b80-9bab-11ea-82d2-f4b60d43ce7e.png)

**Grading Scheme:**

| **Task** | **Grade** | **Grading Criterion** |
| --------------- | --------------- | --------------- |
| Plane Estimate | 30% | A full mark is awarded if the plane parameters are within a tolerance of 0.1 from the correct plane parameters. |
| Lane Boundary Estimation | 40% | Each lane is out of 20%, to be rewarded if the lane boundaries coordinates are within 10 pixels from the correct coordinates. |
| Minimum Distance To Impact | 30% | There should be two distance estimates for two objects that remain after filtering, and 15% is rewarded per object if the error in distance estimation is less than 0.5 meters. |

After finishing the Jupyter notebook for this assessment, please fill in the provided output.yaml file according to the output of the last section. Submit the output.yaml file only.
