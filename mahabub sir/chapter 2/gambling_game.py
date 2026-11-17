import random

# Ask the user how many games they want to play
total_games = int(input("Enter how many games you want to play: "))

win_count = 0  # Counts total games won
loss_count = 0  # Counts total games lost
total_cost = 0  # Total dollars spent ($1 per flip)
total_prize = 0  # Total dollars won ($8 per win)

print("\nGame\tFlip\tRandom No.\tH/T\tHeads\tTails\tDifference")
print("-" * 75)

# Loop through each game
for game in range(1, total_games + 1):
  heads = 0
  tails = 0
  won = False  # Tracks if the player won this game

  # Flip the coin at most 8 times per game
  for flip in range(1, 9):
    # Generate a random number between 0 and 9
    rn = random.randint(0, 9)

    # Pay $1 for each flip
    total_cost = total_cost + 1

    # 0 to 4 is Head, 5 to 9 is Tail
    if rn <= 4:
      outcome = "H"
      heads = heads + 1
    else:
      outcome = "T"
      tails = tails + 1

    # Calculate the difference between heads and tails
    diff = abs(heads - tails)

    # Print the step in table format
    if flip == 1:
      print(f"{game}\t{flip}\t{rn}\t\t{outcome}\t{heads}\t{tails}\t{diff}")
    else:
      print(f"\t{flip}\t{rn}\t\t{outcome}\t{heads}\t{tails}\t{diff}")

    # Check if the difference reaches 3 within 8 flips
    if diff == 3:
      won = True
      break  # Stop flipping because the game is won

  # Check final status of the current game
  if won == True:
    win_count = win_count + 1
    total_prize = total_prize + 8  # Add $8 reward
    print(f"\t\t\t\t\t\tResult: WIN ($8)")
  else:
    loss_count = loss_count + 1
    print(f"\t\t\t\t\t\tResult: LOSS ($0)")

  print("-" * 75)

# Print final summary after all games finish
print("\n=== FINAL GAME SUMMARY ===")
print(f"Total Games Played : {total_games}")
print(f"Total Wins         : {win_count}")
print(f"Total Losses       : {loss_count}")
print(f"Total Cost Paid    : ${total_cost}")
print(f"Total Prize Won    : ${total_prize}")

if total_prize > total_cost:
  print(f"Net Profit         : +${total_prize - total_cost}")
elif total_prize < total_cost:
  print(f"Net Loss           : -${total_cost - total_prize}")
else:
  print("Net Result         : $0 (Break-even)")