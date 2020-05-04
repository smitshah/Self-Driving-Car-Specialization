from math import cos, sin, pi
import numpy as np
from numpy.linalg import inv

def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor
    frame. The values of epsilon and alpha are given in radians, while 
    r is in metres. Epsilon is the elevation angle and alpha is the
    azimuth angle (i.e., in the x,y plane).
    """

    p = np.zeros(3)  # Position vector 

    # Your code here
    p[0] = r * cos(alpha) * cos(epsilon)
    p[1] = r * sin(alpha) * cos(epsilon)
    p[2] = r * sin(epsilon)

    return p

def estimate_params(P):
    """
    Estimate parameters from sensor readings in the Cartesian frame.
    Each row in the P matrix contains a single 3D point measurement;
    the matrix P has size n x 3 (for n points). The format is:
  
    P = [[x1, y1, z1],
         [x2, x2, z2], ...]
       
    where all coordinate values are in metres. Three parameters are
    required to fit the plane, a, b, and c, according to the equation
    
    z = a + bx + cy
    
    The function should retrn the parameters as a NumPy array of size
    three, in the order [a, b, c].
    """

    param_est = np.zeros(3)
    A = np.ones_like(P)
    b = np.zeros((P.shape[0], 1))

      # Your code here
    for i, meas in enumerate(P):
      A[i, 1], A[i, 2], b[i] = meas

    params = inv(A.T @ A) @ A.T @ b
    param_est[0] = params[0, 0]
    param_est[1] = params[1, 0]
    param_est[2] = params[2, 0]

    return param_est

meas = np.array([[pi/3, 0, 5],
                 [pi/4, pi/4, 7],
                 [pi/6, pi/2, 4],
                 [pi/5, 3*pi/4, 6],
                 [pi/8, pi, 3]])
P = np.array([sph_to_cart(*row) for row in meas])
print(estimate_params(P))
