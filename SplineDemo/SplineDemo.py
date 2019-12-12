'''
This demo is from SciPy
https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html#spline-interpolation-in-1-d-procedural-interpolate-splxxx
'''
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt

# Cubic Spline
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x, y, s=0)           # The normal output is a 3-tuple,(t,c,k), containing the knot-points,t,
xnew = np.arange(0, 2*np.pi, np.pi/50)        # the coefficients c and the order k of the spline.
ynew = interpolate.splev(xnew, tck, der=0)

plt.figure(1)
plt.subplot(3, 1, 2)                          # subplot(nrows, ncols, plot number)
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.title('Cubic-spline interpolation')

# First derivative
yder = interpolate.splev(xnew, tck, der=1)
plt.subplot(3, 1, 3)
plt.plot(xnew, yder, xnew, np.cos(xnew), '--')
plt.legend(['Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Derivative estimation from spline')


# Integral of the spline
def integ(x, tck, constant=-1):
    x = np.atleast_1d(x)
    out = np.zeros(x.shape, dtype=x.dtype)
    for n in range(len(out)):
        out[n] = interpolate.splint(0, x[n], tck)
    out += constant
    return out


yint = integ(xnew, tck)
plt.subplot(3, 1, 1)
plt.plot(xnew, yint, xnew, -np.cos(xnew), '--')
plt.legend(['Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Integral estimation from spline')
plt.show()
