import numpy as np
import matplotlib.pyplot as plt

C = 4

def f(n):
    r = np.math.factorial(n) / (np.math.factorial(C) * np.math.factorial(n - C))
    if r > 15e6:
        print n
    return r

x = np.arange(5, 256)
y = map(f, x)

plt.plot(x, y)
plt.show()
