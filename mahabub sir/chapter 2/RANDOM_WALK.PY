# Random Walk Simulation (Beginner Friendly)
# Based on Example 2.5 from the Simulation & Modeling textbook

# 1. Starting coordinates on the X-Y scale
x = 0
y = 0

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

  # Print the result of each step
  print(f"{step:<6} {rn:<12} {direction:<12} ({x}, {y})")

# 4. Print the final result
print("-" * 48)
print(f"Final Location after 20 steps: ({x} cm, {y} cm)")