# Lesson 1 Practice Notebook: Least Squares

In this assignment you will implement the batch least squares method from Module 1, Lesson 1 - "Squared Error Criterion and the Method of Least Squares."

**(Practice) Assignment Overview**

You (an electrical engineer) wish to determine the resistance of an electrical component by using Ohm's law. You recall from your high school circuit classes that ***V = RI***, where ***V*** is the voltage in volts, ***R*** is the resistance in ohms, and ***I*** is the electrical current in amperes. 

Your goal is to:

1. Fit a line through the origin (i.e., determine the parameter **a** for **y=ax**) to this data by using the method of least squares. You may assume that all measurements are of equal importance.
2. Consider what the best estimate of the resistance is in ohms is for this component.



# Lesson 2: Practice Notebook: Recursive Least Squares

In this assignment, you will convert your batch least squares solution to a recursive solution!

**(Practice) Assignment Overview**

You will be implementing the recursive least squares method as described in Module 1, Lesson 2 - "Recursive Least Squares". This time, you will be fitting a line model which includes an offset **y = ax + b**. If Ohm's law (***V = RI***) holds, you expect the offset **b** to be near 0.

While this assignment is not graded, it is important that you have a good grasp of the concepts involved before moving on to the Kalman filter in the next module. Therefore, we encourage you to experiment with the assignment parameters, observing the effects of changing their values!
