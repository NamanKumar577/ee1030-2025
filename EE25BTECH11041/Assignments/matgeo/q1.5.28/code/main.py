import ctypes
import numpy as np
import matplotlib.pyplot as plt

# --- Ctypes Setup ---

# Load the shared library. 
# Make sure 'maine.so' is in the same directory as this Python script,
# or provide the full path to it.
try:
    c_lib = ctypes.CDLL('./main.so')
except OSError as e:
    print(f"Error loading shared library: {e}")
    print("Please ensure 'maine.so' is in the same directory as this script.")
    exit()

# Define the argument types for the C function.
# The C function signature is:
# void trisec(double x1, double y1, double x2, double y2, double* x, double* y)
c_lib.trisec.argtypes = [
    ctypes.c_double, 
    ctypes.c_double, 
    ctypes.c_double, 
    ctypes.c_double, 
    ctypes.POINTER(ctypes.c_double), 
    ctypes.POINTER(ctypes.c_double)
]

# Define the return type of the function.
c_lib.trisec.restype = None

# --- Calculation ---

# Define the input coordinates for the two endpoints of the line segment
x1, y1 = 7.0, 2.0
x2, y2 = 1.0, 5.0

# Prepare ctypes variables to hold the results.
# These will act as the pointers that the C function will write to.
tx = ctypes.c_double()
ty = ctypes.c_double()

# Call the C function from Python to calculate the trisection point
c_lib.trisec(x1, y1, x2, y2, ctypes.byref(tx), ctypes.byref(ty))

# Extract the float values from the ctypes variables
tx_val, ty_val = tx.value, ty.value
print(f"Line segment from ({x1}, {y1}) to ({x2}, {y2})")
print(f"Trisection point calculated by C code: ({tx_val:.2f}, {ty_val:.2f})")


# --- Plotting ---

# Create the plot
plt.figure(figsize=(8, 6))

# Plot the full line segment
plt.plot([x1, x2], [y1, y2], 'g--', label="Line Segment")

# Plot the endpoints of the line
plt.scatter([x1, x2], [y1, y2], color="red", s=100, zorder=5, label="Endpoints")
plt.text(x1, y1 - 0.5, f"A ({x1:.1f}, {y1:.1f})", color="red", fontsize=10)
plt.text(x2, y2 - 0.5, f"B ({x2:.1f}, {y2:.1f})", color="red", fontsize=10)

# Plot the calculated trisection point
plt.scatter(tx_val, ty_val, color="blue", marker="X", s=150, zorder=5, label="Trisection Point")
plt.text(tx_val, ty_val + 0.3, f"Trisection Pt\n({tx_val:.2f}, {ty_val:.2f})", color="blue", fontsize=10)

# Configure plot appearance
plt.title("Line Segment and its Trisection Point")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend(loc="upper left")
plt.grid(True)
plt.axis("equal") # Ensures the scaling is the same on both axes
plt.show()

