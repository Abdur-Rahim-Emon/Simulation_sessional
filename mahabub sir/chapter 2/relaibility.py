import random

TOTAL_HOURS = 10000 # প্রশ্নে দেওয়া মোট সময়

# =========================================================
# POLICY 1: PRESENT POLICY (একটি করে বিয়ারিং পরিবর্তন)
# বইয়ের Table 2.7 অনুযায়ী প্রতিটি বিয়ারিং আলাদাভাবে সিমুলেট হবে
# =========================================================
b1_lives = []  # Policy 2-তে একই লাইফ ব্যবহার করার জন্য সেভ করে রাখব
b2_lives = []
b3_lives = []

total_bearings_p1 = 0
total_delay_p1 = 0

for b in range(1, 4):
  print(f"\n--- PRESENT POLICY: BEARING {b} ---")
  print("RD_Life\tLife\tClock\tRD_Delay\tDelay")

  clock = 0
  while clock < TOTAL_HOURS:
    # ১. Table A থেকে Bearing Life বের করা
    r1 = random.randint(1, 100)
    if r1 <= 10:
      life = 1200
    elif r1 <= 35:
      life = 1400
    elif r1 <= 65:
      life = 1600
    elif r1 <= 90:
      life = 1800
    else:
      life = 2000

    # Policy 2-এর জন্য লাইফগুলো জমা রাখা (বইয়ের নিয়ম অনুযায়ী)
    if b == 1:
      b1_lives.append(life)
    elif b == 2:
      b2_lives.append(life)
    else:
      b3_lives.append(life)

    clock = clock + life

    # ২. Table B থেকে Delay Time বের করা
    r2 = random.randint(1, 10)
    if r2 <= 2:
      delay = 2
    elif r2 <= 5:
      delay = 3
    elif r2 <= 8:
      delay = 4
    else:
      delay = 8

    # টেবিলের রো প্রিন্ট করা
    print(f"{r1}\t{life}\t{clock}\t{r2}\t\t{delay}")

    # ৪০০,০০০ ঘণ্টার মধ্যে ফেইল করলে হিসাব যোগ হবে
    if clock <= TOTAL_HOURS:
      total_bearings_p1 = total_bearings_p1 + 1
      total_delay_p1 = total_delay_p1 + delay

# --- Policy 1 এর খরচের হিসাব (বইয়ের পৃষ্ঠা ২৮ অনুযায়ী) ---
change_time_p1 = total_bearings_p1 * 15  # ১টি বিয়ারিং বদলাতে ১৫ মিনিট
downtime_p1 = total_delay_p1 + change_time_p1

cost_bearing_p1 = total_bearings_p1 * 30  # প্রতি বিয়ারিং $30
cost_downtime_p1 = downtime_p1 * 5  # ডাউনটাইম প্রতি মিনিট $5
cost_tech_p1 = change_time_p1 * (30 / 60)  # টেকনিশিয়ান ঘণ্টায় $30
total_cost_p1 = cost_bearing_p1 + cost_downtime_p1 + cost_tech_p1

print("\n>>> COST CALCULATION FOR POLICY 1 <<<")
print("Total Bearings Replaced =", total_bearings_p1)
print("Total Delay Time        =", total_delay_p1, "minutes")
print("Replacement Time        =", change_time_p1, "minutes")
print("Total Downtime          =", downtime_p1, "minutes")
print("Cost of bearings        = $", cost_bearing_p1)
print("Cost of downtime        = $", cost_downtime_p1)
print("Cost of technician      = $", cost_tech_p1)
print("TOTAL COST (POLICY 1)   = $", total_cost_p1)


# =========================================================
# POLICY 2: PROPOSED POLICY (সবগুলো বিয়ারিং একসাথে পরিবর্তন)
# বইয়ের Table 2.8 অনুযায়ী ৩টি বিয়ারিং একসাথে সিমুলেট হবে
# =========================================================
print("\n\n--- PROPOSED POLICY (ALL 3 BEARINGS TOGETHER) ---")
print("B1_Life\tB2_Life\tB3_Life\tFirst_Fail\tClock\tRD_Delay\tDelay")

clock = 0
breakdowns_p2 = 0
total_delay_p2 = 0
i = 0  # আগের সেভ করা লাইফগুলো নেওয়ার জন্য ইনডেক্স

while clock < TOTAL_HOURS:
  # আগের লিস্টে লাইফ থাকলে সেখান থেকে নেবে, শেষ হয়ে গেলে নতুন র‍্যান্ডম লাইফ নেবে
  if i < len(b1_lives):
    life1 = b1_lives[i]
  else:
    r = random.randint(1, 100)
    if r <= 10:
      life1 = 1200
    elif r <= 35:
      life1 = 1400
    elif r <= 65:
      life1 = 1600
    elif r <= 90:
      life1 = 1800
    else:
      life1 = 2000

  if i < len(b2_lives):
    life2 = b2_lives[i]
  else:
    r = random.randint(1, 100)
    if r <= 10:
      life2 = 1200
    elif r <= 35:
      life2 = 1400
    elif r <= 65:
      life2 = 1600
    elif r <= 90:
      life2 = 1800
    else:
      life2 = 2000

  if i < len(b3_lives):
    life3 = b3_lives[i]
  else:
    r = random.randint(1, 100)
    if r <= 10:
      life3 = 1200
    elif r <= 35:
      life3 = 1400
    elif r <= 65:
      life3 = 1600
    elif r <= 90:
      life3 = 1800
    else:
      life3 = 2000

  i = i + 1

  # ৩টির মধ্যে যেটি সবার আগে নষ্ট হবে (Minimum Life)
  first_fail = min(life1, life2, life3)
  clock = clock + first_fail

  # Delay Time বের করা
  r2 = random.randint(1, 10)
  if r2 <= 2:
    delay = 2
  elif r2 <= 5:
    delay = 3
  elif r2 <= 8:
    delay = 4
  else:
    delay = 8

  print(
      f"{life1}\t{life2}\t{life3}\t{first_fail}\t\t{clock}\t{r2}\t\t{delay}"
  )

  if clock <= TOTAL_HOURS:
    breakdowns_p2 = breakdowns_p2 + 1
    total_delay_p2 = total_delay_p2 + delay

# --- Policy 2 এর খরচের হিসাব (বইয়ের পৃষ্ঠা ২৯-৩০ অনুযায়ী) ---
total_bearings_p2 = breakdowns_p2 * 3  # প্রতিবার ৩টি করে বিয়ারিং বদলানো হয়
change_time_p2 = breakdowns_p2 * 35  # ৩টি বিয়ারিং বদলাতে ৩৫ মিনিট লাগে
downtime_p2 = total_delay_p2 + change_time_p2

cost_bearing_p2 = total_bearings_p2 * 30  # প্রতি বিয়ারিং $30
cost_downtime_p2 = downtime_p2 * 5  # ডাউনটাইম প্রতি মিনিট $5
cost_tech_p2 = change_time_p2 * (30 / 60)  # টেকনিশিয়ান ঘণ্টায় $30
total_cost_p2 = cost_bearing_p2 + cost_downtime_p2 + cost_tech_p2

print("\n>>> COST CALCULATION FOR POLICY 2 <<<")
print("Total Breakdowns        =", breakdowns_p2)
print("Total Bearings Replaced =", total_bearings_p2)
print("Total Delay Time        =", total_delay_p2, "minutes")
print("Replacement Time        =", change_time_p2, "minutes")
print("Total Downtime          =", downtime_p2, "minutes")
print("Cost of bearings        = $", cost_bearing_p2)
print("Cost of downtime        = $", cost_downtime_p2)
print("Cost of technician      = $", cost_tech_p2)
print("TOTAL COST (POLICY 2)   = $", total_cost_p2)

# =========================================================
# FINAL DECISION
# =========================================================
print("\n==========================================")
if total_cost_p2 < total_cost_p1:
  print("DECISION: Proposed Policy is BETTER!")
  print("Total Savings = $", total_cost_p1 - total_cost_p2)
else:
  print("DECISION: Present Policy is BETTER!")
  print("Total Savings = $", total_cost_p2 - total_cost_p1)