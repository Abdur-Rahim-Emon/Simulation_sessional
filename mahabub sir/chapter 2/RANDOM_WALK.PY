import matplotlib.pyplot as plt

# 1. Starting coordinates on the X-Y scale
x = 0
y = 0

# Lists to record every position for plotting (starting at 0, 0)
x_path = [0]
y_path = [0]

# 2. List of random numbers given in the question (we will use the first 20)
random_numbers = [6, 2, 0, 6, 2, 8, 5, 7, 7, 9, 8, 4, 8, 2, 6, 2, 1, 3, 0, 8, 4]

# Print table header
print(f"{'Step':<6} {'Random No.':<12} {'Direction':<12} {'Position (X, Y)'}")
print("-" * 48)

# 3. Loop through 20 steps
for step in range(1, 21):
  rn = random_numbers[step - 1]  # Get the random number for the current step

  # Check which direction the random number corresponds to
  if rn == 0:
    direction = "Backward"
    y = y - 30  # Move 30 cm backward
  elif 1 <= rn <= 5:
    direction = "Forward"
    y = y + 80  # Move 80 cm forward
  elif rn == 6:
    direction = "Right"
    x = x + 60  # Move 60 cm right
  else:  # rn is 7, 8, or 9
    direction = "Left"
    x = x - 40  # Move 40 cm left

  # Save the updated coordinates into our path lists
  x_path.append(x)
  y_path.append(y)

  # Print the result of each step
  print(f"{step:<6} {rn:<12} {direction:<12} ({x}, {y})")

# 4. Print the final result
print("-" * 48)
print(f"Final Location after 20 steps: ({x} cm, {y} cm)")

# ==============================================================================
# 5. Plot the Movement Trace (Matching Fig. 2.5 in Textbook Page 26)
# ==============================================================================
plt.figure(figsize=(8, 7))

# Draw the step-by-step path line with dots at each stop
plt.plot(
    x_path,
    y_path,
    color="black",
    linewidth=1.5,
    marker="o",
    markersize=4,
    label="Walk Path",
)

# Add directional arrows for each step (just like Fig. 2.5)
for i in range(len(x_path) - 1):
  plt.annotate(
      "",
      xy=(x_path[i + 1], y_path[i + 1]),
      xytext=(x_path[i], y_path[i]),
      arrowprops=dict(arrowstyle="->", color="blue", lw=1.2),
  )

# Highlight the Start (0, 0) and Final Position
plt.scatter(
    [0], [0], color="green", s=100, zorder=5, label="Start Point (0, 0)"
)
plt.scatter(
    [x], [y], color="red", s=100, zorder=5, label=f"End Point ({x}, {y})"
)

# Draw X and Y axes through (0, 0) like the textbook diagram
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

# Labels, title, grid, and legend
plt.title("Random Walk Simulation Trace (20 Steps)", fontsize=13)
plt.xlabel("X-axis (cm)", fontsize=11)
plt.ylabel("Y-axis (cm)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(loc="best")
plt.tight_layout()

# Display the plot
plt.show()
