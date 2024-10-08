import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

fig, (ax1, ax2) = plt.subplots(1,2)
fig.set_facecolor("red")
ax1.set_facecolor("blue")
ax1.plot(x,y)
ax2.set_facecolor("yellow")
