import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

# draw sphere
u, v = np.mgrid[0:2*np.pi:50j, 0:np.pi:25j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="b")

plt.show()
