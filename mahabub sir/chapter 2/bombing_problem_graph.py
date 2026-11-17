import matplotlib.pyplot as plt

# 1. Random Normal Numbers (RNN) from Textbook Table 2.9 (Page 31)
rnn_x = [0.23, -1.16, 0.39, -1.90, -0.78, -0.02, -0.40, -0.66, 1.41, 0.07, 0.53, 0.03, -1.19, 0.11, 0.16, -0.82, 0.42, -0.89, 0.49, -0.21]

rnn_y = [0.24, -0.02, 0.64, -1.04, 0.68, -0.47, -0.75, -0.44, 1.21, -0.08, -1.56, 1.49, -1.19, -1.86, 1.21, 0.75, -1.50, 0.19, -1.44, 0.65]

total_bombs = len(rnn_x)  # Total 20 bomb strikes (2 sorties x 10 bombers)
hits = 0  # Counter for hits
misses = 0  # Counter for misses

# Lists to store coordinates for plotting the graph
x_hit = []
y_hit = []
x_miss = []
y_miss = []

# Print Table 2.9 header
print("Bomb Strike\tRNN_x\tx\t\tRNN_y\ty\t\tResult")
print("-" * 72)

# 2. Loop through all 20 bomb strikes
for i in range(total_bombs):
  zx = rnn_x[i]
  zy = rnn_y[i]

  # Calculate X and Y strike coordinates (x = 500 * Zx, y = 300 * Zy)
  x = 500 * zx
  y = 300 * zy

  # Check if the bomb lands inside the 1000m x 600m target area (-500 to 500, -300 to 300)
  if -500 <= x <= 500 and -300 <= y <= 300:
    result = "Hit"
    hits = hits + 1
    x_hit.append(x)
    y_hit.append(y)
  else:
    result = "Miss"
    misses = misses + 1
    x_miss.append(x)
    y_miss.append(y)

  # Print each row of Table 2.9
  print(f"{i+1}\t\t{zx:.2f}\t{x:.0f}\t\t{zy:.2f}\t{y:.0f}\t\t{result}")

# 3. Calculate and print final summary (matching textbook page 31)
hit_percentage = (hits / total_bombs) * 100

print("-" * 72)
print(f"Number of hits                = {hits}")
print(f"Number of misses              = {misses}")
print(f"% Number of strikes on target = {hit_percentage:.0f} %")

# ==============================================================================
# 4. Plot the Graph of Bomb Strikes on the Target Area
# ==============================================================================
plt.figure(figsize=(8, 6))

# Draw the rectangular target area (1000m x 600m centered at 0,0)
rect_x = [-500, 500, 500, -500, -500] # graph e position thik korar jnno 
rect_y = [-300, -300, 300, 300, -300]
plt.plot(
    rect_x,
    rect_y,
    color="blue",
    linewidth=2,
    label="Target Area (1000m x 600m)",
)
plt.fill(rect_x, rect_y, color="lightblue", alpha=0.3)

# Plot Hit points (green dots) and Miss points (red crosses)
plt.scatter(x_hit, y_hit, color="green", s=70, zorder=5, label=f"Hit ({hits})")
plt.scatter(
    x_miss, y_miss, color="red", marker="x", s=70, zorder=5, label=f"Miss ({misses})"
)

# Plot the center aiming point (0, 0)
plt.scatter(
    [0], [0], color="black", marker="+", s=120, zorder=6, label="Aiming Point (0, 0)"
)

# Add labels, title, grid, and legend
plt.title("Monte Carlo Simulation of Bombing Problem (Table 2.9)")
plt.xlabel("X-coordinate (meters)")
plt.ylabel("Y-coordinate (meters)")
plt.axhline(0, color="gray", linestyle=":", linewidth=1)
plt.axvline(0, color="gray", linestyle=":", linewidth=1)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper right")

# Show the plot
plt.show()