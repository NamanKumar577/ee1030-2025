import numpy as np
import matplotlib.pyplot as plt

# Normal and direction vectors for 2x + y = 3
normal_vector = np.array([2, 1])
direction_vector = np.array([1, -2])

print(f"Normal Vector (n): {normal_vector}")
print(f"Direction Vector (m): {direction_vector}")

dot_product = np.dot(normal_vector, direction_vector)
print(f"Dot product of n and m: {dot_product}")
if np.isclose(dot_product, 0):
    print("The vectors are orthogonal (as expected).")
else:
    print("The vectors are NOT orthogonal (something is wrong).")

# Line equation: y = 3 - 2x
def line_equation(x):
    return 3 - 2*x

x_vals = np.linspace(-5, 7, 100)
y_vals = line_equation(x_vals)

vector_origin = np.array([2, 4])

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(8, 8))

plt.plot(x_vals, y_vals, label='Line: 2x + y = 3', color='blue', zorder=1)

plt.quiver(vector_origin[0], vector_origin[1],
           direction_vector[0], direction_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='green', label='Direction Vector', zorder=2)

plt.quiver(vector_origin[0], vector_origin[1],
           normal_vector[0], normal_vector[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='Normal Vector', zorder=2)

plt.plot(vector_origin[0], vector_origin[1], 'o', color='purple', markersize=8,
         label='Vector Origin (2, 4)')

plt.title('Line with Direction and Normal Vectors')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axis('equal')
plt.legend()
plt.grid(True)

plt.xlim(-5, 10)
plt.ylim(-5, 10)

plt.savefig("../figs/Figure_2.png")
plt.show()
