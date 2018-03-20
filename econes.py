import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def E(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to cone q at r0."""
    den = ((x-r0[0])**2 + (y-r0[1])**2)**1.5
    # print('q is ' + repr(q))
    # print('x is: ' + repr(x))
    # print('y is: ' + repr(y))
    # print('r0[0] is: ' + repr(r0[0]))
    # print('r0[1] is: ' + repr(r0[1]))
    return q * (y - r0[1]) / den, -q * (x - r0[0]) / den
#    return q * (x - r0[0]) / den, q * (y - r0[1]) / den


# Grid of x, y points
nx, ny = 40, 40
x = np.linspace(-20, 20, nx)
y = np.linspace(-20, 20, ny)
X, Y = np.meshgrid(x, y)

# Create a multipole with nq cones of alternating sign, equally spaced
# on the unit circle.
# nq = 2**int(sys.argv[1])
cones = []

#cones.append((1, (5.0,17.0)))
#cones.append((-1, (-5.0, 17.0)))


cones.append((1, (1.0, 5.0)))
#cones.append((-1, (-1.0, 0.0)))
#cones.append((1, (1.0, -5.0)))
#cones.append((1, (1.0, -10.0)))
#
#cones.append((1, (5.0,-19.0)))
#cones.append((-1, (-5.0, -19.0)))
#cones.append((1, (5.0,-17.0)))
#cones.append((-1, (-5.0, -17.0)))

# print(cones)

# Electric field vector, E=(Ex, Ey), as separate components
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))
for cone in cones:
    ex, ey = E(*cone, x=X, y=Y)
    Ex += ex
    Ey += ey

fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the streamlines with an appropriate colormap and arrow style
color = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

# Add filled circles for the cones themselves
cone_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in cones:
    ax.add_artist(Circle(pos, 0.5, color=cone_colors[q>0]))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)
ax.set_aspect('equal')
plt.show()
