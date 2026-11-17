import matplotlib.pyplot as plt
import numpy as np

# 1. Given random numbers for X and Y coordinates
rx_list = [48, 36, 44, 41, 46, 18, 32, 41, 23, 23]
ry_list = [0.52, 0.18, 0.30, 0.88, 0.21, 0.25, 0.57, 0.82, 0.90, 0.63]

# ==============================================================================
# Optional: If your teacher asks to generate random numbers dynamically,
# uncomment the two lines below (using 20 to 50 for X as per textbook page 22):
# rx_list = np.random.randint(20, 51, 20)  # 20 random integers between 20 and 50
# ry_list = np.random.rand(20)             # 20 random floats between 0 and 1
# ==============================================================================

# 2. Dimensions of the bounding rectangle ABCD (from textbook Fig. 2.2)
width = 5 - 2  # Limits of x are 2 to 5, so width = 3
height = 140  # Height of the rectangle = 140
area_A = height * width  # Total area of rectangle A = 140 * 3 = 420

M = 0  # Counter for points falling under the curve
N = len(rx_list)  # Total number of trials (10 points)

# Lists to store points for plotting the graph
x_inside, y_inside = [], []
x_outside, y_outside = [], []

# Print table header (matching textbook Table 2.2)
print("RN_x\tx = 0.1(r)\tRN_y\ty = 140(r)\tx^3\t\tM\tN")
print("-" * 72)

# 3. Loop through all random points
for i in range(N):
  rx = rx_list[i]
  ry = ry_list[i]

  # Scale random numbers to X and Y coordinates
  x = 0.1 * rx
  y = 140 * ry
  x_cube = x**3

  # Check if the point lies below or on the curve (y <= x^3)
  if y <= x_cube:
    M = M + 1
    x_inside.append(x)
    y_inside.append(y)
  else:
    x_outside.append(x)
    y_outside.append(y)

  # Print each row of the simulation table
  print(f"{rx}\t{x:.1f}\t\t{ry:.2f}\t{y:.2f}\t\t{x_cube:.2f}\t\t{M}\t{i+1}")

# 4. Calculate the simulated integral area
I_simulated = (M / N) * area_A

# 5. Calculate Exact Area and Error (as per textbook page 21)
exact_area = (5**4 / 4) - (2**4 / 4)  # Analytical exact value = 152.25
error = abs(exact_area - I_simulated)  # Absolute error
percentage_error = (error / exact_area) * 100  # Percentage error

print("-" * 72)
print(f"Total points under curve (M) = {M}")
print(f"Total trials (N)             = {N}")
print(
    f"Simulated Area (I)           = ({M}/{N}) * {area_A} = {I_simulated:.2f}"
)
print(f"Exact Area (Analytical)      = {exact_area:.2f}")
print(f"Absolute Error               = {error:.2f}")
print(f"Percentage Error             = {percentage_error:.2f}%")

# ==============================================================================
# 6. Plot the Graph (Matching Textbook Fig. 2.2)
# ==============================================================================
plt.figure(figsize=(8, 6))

# Plot the curve f(x) = x^3
x_curve = np.linspace(0, 5.3, 200)
y_curve = x_curve**3
plt.plot(x_curve, y_curve, color="black", linewidth=2, label="f(x) = x^3")

# Shade the integral area under the curve from x = 2 to x = 5
x_fill = np.linspace(2, 5, 100)
plt.fill_between(
    x_fill,
    x_fill**3,
    color="skyblue",
    alpha=0.4,
    label="Exact Integral Area (152.25)",
)

# Draw the bounding rectangle ABCD (x: 2 to 5, y: 0 to 140)
rect_x = [2, 5, 5, 2, 2]
rect_y = [0, 0, 140, 140, 0]
plt.plot(
    rect_x,
    rect_y,
    color="gray",
    linestyle="--",
    linewidth=1.5,
    label="Bounding Rectangle ABCD (A = 420)",
)

# Plot points under the curve (green) and above the curve (red)
plt.scatter(
    x_inside,
    y_inside,
    color="green",
    s=70,
    zorder=5,
    label=f"Under Curve: y <= x^3 (M = {M})",
)
plt.scatter(
    x_outside,
    y_outside,
    color="red",
    marker="x",
    s=70,
    zorder=5,
    label=f"Above Curve: y > x^3 (N - M = {N - M})",
)

# Add title, labels, grid, and legend
plt.title("Monte Carlo Numerical Integration: Integral of x^3 dx from 2 to 5")
plt.xlabel("X")
plt.ylabel("f(x) = x^3")
plt.xlim(0, 5.8)
plt.ylim(0, 165)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper left")

# Display the graph
plt.show()