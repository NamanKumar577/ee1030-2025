import matplotlib.pyplot as plt
import numpy as np

A = (7, 2)

B = (1, 5)

P = (5, 3)
Q = (3, 4)

fig, ax = plt.subplots(figsize=(10, 7))

ax.plot([A[0], B[0]], [A[1], B[1]], color='skyblue', linestyle='-', linewidth=2, label='Line Segment AB')

points = {'A': A, 'B': B, 'P': P, 'Q': Q}
colors = {'A': 'blue', 'B': 'blue', 'P': 'red', 'Q': 'green'}

for name, (x, y) in points.items():
    ax.scatter(x, y, s=100, color=colors[name], zorder=5) 
    ax.text(x + 0.15, y + 0.15, f'{name}({x}, {y})', fontsize=12, verticalalignment='bottom')

ax.set_title('Trisection of a Line Segment', fontsize=16, fontweight='bold')
ax.set_xlabel('X-axis', fontsize=14)
ax.set_ylabel('Y-axis', fontsize=14)

ax.grid(True, linestyle='--', alpha=0.6)

ax.set_xlim(0, 8)
ax.set_ylim(0, 6)

ax.set_aspect('equal', adjustable='box')

ax.legend()

plt.savefig('trisection_plot.png')
plt.show()
