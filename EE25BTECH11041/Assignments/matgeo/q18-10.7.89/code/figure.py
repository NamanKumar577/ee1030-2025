import numpy as np
import matplotlib.pyplot as plt

line1_coeffs = np.array([5, 12, -10])
line2_coeffs = np.array([5, -12, -40])


A = np.array([[line1_coeffs[0], line1_coeffs[1]],
              [line2_coeffs[0], line2_coeffs[1]]])
b = np.array([-line1_coeffs[2], -line2_coeffs[2]])


intersection_point = np.linalg.solve(A, b) # Returns [5., -1.25]


h = intersection_point[0]

r1 = 3

k = 2
center = np.array([h, k])


intercept_length = 8
half_intercept = intercept_length / 2.0


r2 = np.hypot(r1, half_intercept) # np.hypot(3, 4) = 5


print("--- Solution (calculated with NumPy) ---")
print(f"Intersection of lines: {intersection_point}")
print(f"Center of circles C1 and C2: ({center[0]}, {center[1]})")
print(f"Radius of circle C1: {r1}")
print(f"Radius of circle C2: {r2}")
print("\nThe equation of circle C2 is:")
print(f"(x - {center[0]})**2 + (y - {center[1]})**2 = {r2**2}")
print("-----------------------------------------")



def get_circle_points(center_h, center_k, radius):
    """Generates x and y coordinates for a circle."""
    theta = np.linspace(0, 2 * np.pi, 200)
    x = center_h + radius * np.cos(theta)
    y = center_k + radius * np.sin(theta)
    return x, y


x_c1, y_c1 = get_circle_points(center[0], center[1], r1)
x_c2, y_c2 = get_circle_points(center[0], center[1], r2)


x_vals = np.linspace(-5, 15, 400)


y_line1 = (-line1_coeffs[0] * x_vals - line1_coeffs[2]) / line1_coeffs[1]

y_line2 = (-line2_coeffs[0] * x_vals - line2_coeffs[2]) / line2_coeffs[1]


plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 10))


ax.plot(x_vals, y_line1, 'b-', label='5x + 12y - 10 = 0')
ax.plot(x_vals, y_line2, 'g-', label='5x - 12y - 40 = 0')


ax.plot(x_c1, y_c1, 'r-', label=f'Circle C1: $(x-5)^2 + (y-2)^2 = {r1**2}$')
ax.plot(x_c2, y_c2, 'm--', label=f'Circle C2: $(x-5)^2 + (y-2)^2 = {r2**2}$')

ax.plot(center[0], center[1], 'ko', markersize=8, label=f'Center ({center[0]}, {center[1]})')


ax.set_title('Geometric Solution of Circles and Lines', fontsize=16)
ax.set_xlabel('x-axis', fontsize=12)
ax.set_ylabel('y-axis', fontsize=12)
ax.legend(fontsize=10)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)

ax.set_aspect('equal', adjustable='box')
plt.savefig("figure.png", dpi=300)
plt.show()


