import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8, 8, 0.1)

y = np.tanh(x)

plt.plot(x, y, lw=3)
plt.xlim(-8, 8) 
plt.ylim(-1.5, 1.5) 
plt.grid() 
plt.show() 
