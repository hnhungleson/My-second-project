import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
print("X")
print(x.flatten())
y = np.sin(u)*np.sin(v)
print("Y")
print(y.flatten())
z = np.cos(v)
print("Z")
print(z.shape)
print(z.flatten())


# ax.plot_wireframe(x, y, z, color="b", linewidth=0.2)
ax.plot_surface(x.flatten(), y.flatten(), z.flatten().reshape([len(z.flatten()), 1]), color="b")
plt.show()
