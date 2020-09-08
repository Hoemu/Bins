import matplotlib.pyplot as plt
import numpy as np
import math
import pandans

x = np.linspace(math.pi, 30.0, 10000)
y = np.sinh(x)

y1= np.random.randn(100)

plt.plot(x, y, ls = "-", lw = 2, c = "c", label = "plot figure", color = "blue")
plt.legend()
plt.axhline(y=0.0,  c = "r", ls = "--", lw = 2)
plt.axvline(x=4.0,  c = "r", ls = "--", lw = 2)
plt.show()

'''
x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
plt.plot(x, y, ls ="-", label = "plot figure")
plt.legend()
plt.show()
'''