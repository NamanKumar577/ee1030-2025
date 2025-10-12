import ctypes
import numpy as np
import matplotlib.pyplot as plt


lib = ctypes.CDLL('./main.so')


lib.get_circles.argtypes = [
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)
]


h1 = ctypes.c_double()
k1 = ctypes.c_double()
r1 = ctypes.c_double()
h2 = ctypes.c_double()
k2 = ctypes.c_double()
r2 = ctypes.c_double()

# Call C function
lib.get_circles(ctypes.byref(h1), ctypes.byref(k1), ctypes.byref(k2), ctypes.byref(h2), ctypes.byref(k2), ctypes.byref(r2))

# But fix: k2 got used twice → fix proper call
lib.get_circles(ctypes.byref(h1), ctypes.byref(k1), ctypes.byref(r1), ctypes.byref(h2), ctypes.byref(k2), ctypes.byref(r2))

# Extract values
h1, k1, r1 = h1.value, k1.value, r1.value
h2, k2, r2 = h2.value, k2.value, r2.value

# Plot circles and lines
theta = np.linspace(0, 2*np.pi, 400)
x1, y1 = h1 + r1*np.cos(theta), k1 + r1*np.sin(theta)
x2, y2 = h2 + r2*np.cos(theta), k2 + r2*np.sin(theta)

plt.figure(figsize=(7,7))
plt.plot(x1, y1, 'b', label='Circle C1')
plt.plot(x2, y2, 'g', label='Circle C2')

# Plot lines
x = np.linspace(-5, 15, 400)
y_line1 = (-5*x + 10)/12
y_line2 = (5*x - 40)/12
plt.plot(x, y_line1, 'r--', label='Line 1')
plt.plot(x, y_line2, 'r-.', label='Line 2')

# Format plot
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.legend()
plt.title('Circles C1 & C2 with Tangent Lines')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

