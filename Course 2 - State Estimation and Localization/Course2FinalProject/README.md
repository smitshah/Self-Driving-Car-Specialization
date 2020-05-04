# Vehicle State Estimation on a Roadway

In this assignment, you will implement the Error-State Extended Kalman Filter (ES-EKF) to localize a vehicle using data from the CARLA simulator. The project has three parts, which should be completed in sequence:

1. First, you will fill in the skeleton implementation of the ES-EKF that is provided, by writing code to perform the filter prediction step and the correction step. The filter relies on IMU data to propagate the state forward in time, and GPS and LIDAR position updates to correct the state estimate. For **Part 1** of the project, the sensor data have been prepackaged for you - it is possible to visualize the output of the estimator and compare it to the ground truth vehicle position (the ground truth position data are also provided). Your complete filter implementation will be tested by comparing the estimated vehicle position (produced by your code) with the ground truth position, for a 'hold out' portion of the trajectory (i.e., for which ground truth is not provided to you).

2. In **Part 2**, you will examine the effects of sensor miscalibration on the vehicle pose estimates. Specifically, you will uncomment a block of code that intentionally alters the transformation between the LIDAR sensor frame and the IMU sensor frame; use of the incorrect transform will result in errors in the vehicle position estimates. After looking at the errors, your task is to determine how to adjust the filter parameters (noise variances) to attempt to compensate for these errors. The filter code itself should remain unchanged. Your updated filter (with the new parameter(s)) will be tested in the same way as in Part 1.

3. In **Part 3**, you will explore the effects of sensor dropout, that is, when all external positioning information (from GPS and LIDAR) is lost for a short period of time. For Part 3, you will load a different dataset where a portion of the GPS and LIDAR measurements are missing (see the detailed instructions below). The goal of Part 3 is to illustrate how the loss of external corrections results in drift in the vehicle position estimate, and also to aid in understanding how the uncertainty in the position estimate changes when sensor measurements are unavailable.

To complete the filter implementation, you will need to fill in sections of the skeleton ES-EKF file that are marked with the comments "4. Measurement Update" and "5. Main Filter Loop." The equations you will use are discussed in Lesson 2 of the module. In order to generate the required output for each part of the project, you will uncomment a portion of the code as described in the “Getting outputs for Submission” section below. ***Note:*** You do not need to produce the output files yourself - the Coursera grader is expecting a specific format, which is already produced automatically for you.

**Instructions for Getting Started**

Begin by downloading c2m5_assignment_files.tar.gz file from the link below.

[c2m5_assignment_files.tar.gz](https://d3c33hcgiwev3.cloudfront.net/_O40qaTGEemW8A5odpwTWA_a5efdea38be244a8a766b7b3d1ad24d7_c2m5_assignment_files.tar.gz?Expires=1588723200&Signature=MFvitjr7T9msOof62lK-CtKXIN7g4tay~B8IGVZHvqch2JpcnjM3W4zg8tPlpYJCz3ILIICCFhxPpWTd5DK2geTg60KqJwjPAt-Y2KSlnRm2hM67vmkBOmYYe~l2FiPqX7d6UYoNuz0sv7WtcXIAFW0BtdqakrKW4ByuqROBv8M_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

In it, you'll find es_ekf.py, rotations.py, and a folder labelled data, as shown below.

![cf1](https://user-images.githubusercontent.com/42312238/80974218-0b7bca00-8e3e-11ea-9d0d-05b2369653ac.png)

You will be adding code to the es_ekf.py file to complete the sections that are missing, based on what you have learned in this course. The data folder contains the data you will use for the project, and the rotations.py file contains a Quaternion class and other rotation-related functions that are already implemented for you.

![cf2](https://user-images.githubusercontent.com/42312238/80974237-120a4180-8e3e-11ea-97d9-096ea522bc83.png)

There are a large number of block comments throughout es_ekf.py. Take a look at the comments to try to understand what each section of the code is doing, and in particular to understand all of the data contained in the Python pickle (pkl) files. As the code runs, some visualizations (plots) will already appear for you, including a plot of the ground truth trajectory, a plot of the ground truth trajectory compared to your estimated trajectory, and six error plots.

To run es_ekf.py, simply call 'python es_ekf.py' from the command line or 'run es_ekf.py' from within an interactive shell.

![cf3](https://user-images.githubusercontent.com/42312238/80974251-18002280-8e3e-11ea-878b-e2aec76ce7c8.png)

**Getting Output for Submission**

You will be submitting text files to Coursera that contain a set of position estimates determined by your filter. To generate your submission text files, you'll have to ensure that the correct parts of the code are commented/uncommented.

In the 'Data' section of the code, you'll see the following line:

```python3
with open('student_data/pt1_data.pkl', 'rb') as file:
    data = pickle.load(file)
```

Ensure that you leave this as pt1_data.pkl for Parts 1 and 2. For Part 3, switch it to pt3_data.pkl.

The following block of code defines the calibration rotation matrix that determines the rotation between the LIDAR sensor frame and the IMU frame.

```python3
# This is the correct calibration rotation matrix, corresponding to an euler rotation of 0.05, 0.05, .1.
C_li = np.array([
    [ 0.99376, -0.09722,  0.05466],
    [ 0.09971,  0.99401, -0.04475],
    [-0.04998,  0.04992,  0.9975 ]
])

# This is an incorrect calibration rotation matrix, corresponding to a rotation of 0.05, 0.05, 0.05
# C_li = np.array([
#     [ 0.9975 , -0.04742,  0.05235],
#     [ 0.04992,  0.99763, -0.04742],
#     [-0.04998,  0.04992,  0.9975 ]
# ])
```

Ensure that you leave the top lines uncommented for Parts 1 and 3, but leave the bottom lines uncommented for Part 2.

As well, at the bottom of the file, you'll see three blocks that look like this:

```python3
# Pt. 1 submission
pt1_indices = [9000, 9400, 9800, 10200, 10600]
pt1_str = ''
for val in pt1_indices:
    for i in range(3):
        p1_str += str(p_est[val, i]) + ' '
with open('pt1_submission.txt', 'w') as file:
    file.write(p1_str)
```

Ensure that the lines under Pt. 1 submission are uncommented for Part 1, the lines under Pt. 2 submission are uncommented for Part 2, and the lines under Pt. 3 submission are uncommented for Part 3. This will generate the right set of output data for each portion of the assignment.

When you're ready to submit, you should have three separate txt files titled ptx_submission.txt, where x is the part number.

![cf4](https://user-images.githubusercontent.com/42312238/80974267-1c2c4000-8e3e-11ea-80f8-5dd7d04b0bdb.png)

You will receive 20% of your grade for each part, for each position estimate that is within a certain threshold of the ground truth position. Note that a portion of the ground truth trajectory is 'held back' for testing (so you won't see the entire ground truth trajectory).


**Tricks and Tips**

The final project is challenging! Here are a few tricks and tips to help you get started and to assist in debugging your code:

1. For Part 1 (and Parts 2 and 3), be sure to be very careful to properly treat the orientation states (i.e., states that involve rotations). As discussed in the course lessons, (sometimes small) errors when dealing with rotations can result in significant and difficult-to-diagnose bugs. Be sure to double check!

2. For Part 2, you will change the extrinsic calibration of the LIDAR sensor relative to the vehicle frame. This (purposefully) results in a systematic modelling error - what effect will this have on the estimator performance (recall the lesson on sensor calibration...)? To achieve better performance, you may need to adjust the variance of the LIDAR measurements in the filter (the variable 'var_lidar'). What change could you make to attempt to deal with a modelling error?

3. For Part 3, you will examine what happens when positioning information from the GPS receiver and the LIDAR 'drops out'. In this situation, the filter will propagate the motion model forward in time, using the IMU measurements to dead reckon. During the period where positioning updates are unavailable, how would you expect the variance (uncertainty) in the position states (x, y, z) to change? Should the filter remain consistent?


***Good luck!***
