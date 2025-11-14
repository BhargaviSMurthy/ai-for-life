from scipy import optimize
from scipy import integrate
import numpy as np
# Define a function
def scipy(x):
    return (x - 3)**2 + 5

# Use SciPy to find the minimum
result = optimize.minimize(scipy, x0=0)

print("Minimum value:", result.fun)
print("At x =", result.x)



# Define the function to integrate
def func(x):
    return np.sin(x)

# Integrate sin(x) from 0 to π
result, error = integrate.quad(func, 0, np.pi)

print("Integral:", result)
print("Error:", error)
