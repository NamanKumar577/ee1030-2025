import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


x = np.array([3 ,3]).reshape(-1,1)
y= np.array([3,1])
m = np.array([[0.8,-0.6],[0.6,0.8]])
fig, ax = plt.subplots()

ax.arrow(0, 0, 3, 3, head_width=0.1, head_length=0.1, fc='blue', ec='blue', label="vector A")
c = m@x
ax.arrow(0, 0, c[0,0], c[1,0], head_width=0.1, head_length=0.1, fc='pink', ec='pink',label="result vector,MA")



center = (0, 0)
radius = 1.0
start_angle = 45
end_angle = 81.87

arc = Arc(center, 2 * radius, 2 * radius, theta1=start_angle, theta2=end_angle, 
          edgecolor='orange', linewidth=1)

ax.add_patch(arc)
ax.add_patch(arc)



ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
plt.legend()
plt.grid()
plt.savefig("fig1.png", dpi=300)
plt.show()
