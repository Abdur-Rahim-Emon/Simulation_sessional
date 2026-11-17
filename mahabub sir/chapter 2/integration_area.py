
#import numpy as np

rx_list = [48, 36, 44, 41, 46, 18, 32, 41, 23, 23]
ry_list = [0.52, 0.18, 0.30, 0.88, 0.21, 0.25, 0.57, 0.82, 0.90, 0.63]
#====================================
#if sir tell genterate random numbers 
"""
rx_list=np.random.randint(1,101,20)#1 to 100 20 random numbers 
ry_list=np.random.rand(20)  # 0 to 1 total 20 random numbers
"""
#==================================
# ২. বইয়ের দেওয়া আয়তক্ষেত্রের মাপ (Rectangle ABCD)
width = 5 - 2  # x এর সীমা 2 থেকে 5, তাই প্রস্থ = 3
height = 140  # বইয়ের চিত্র অনুযায়ী উচ্চতা = 140
area_A = height * width  # মোট ক্ষেত্রফল A = 140 * 3 = 420

M = 0  # কার্ভের নিচে কয়টি বিন্দু পড়ল তা গুনবে
N = len(rx_list)  # মোট ট্রায়াল সংখ্যা (১০টি)

# টেবিলের হেডার প্রিন্ট করা (বইয়ের Table 2.2 এর মতো)
print("RN_x\tx = 0.1(r)\tRN_y\ty = 140(r)\tx^3\t\tM\tN")
print("-" * 72)

# ৩. ১০টি বিন্দুর জন্য লুপ চালানো
for i in range(N):
  rx = rx_list[i]
  ry = ry_list[i]

  # বইয়ের সূত্র অনুযায়ী x, y এবং x^3 বের করা
  x = 0.1 * rx
  y = 140 * ry
  x_cube = x**3

  # যদি y <= x^3 হয়, তবে বিন্দুটি কার্ভের নিচে পড়েছে
  if y <= x_cube:
    M = M + 1

  # প্রতিটি রো প্রিন্ট করা
  print(f"{rx}\t{x:.1f}\t\t{ry:.2f}\t{y:.2f}\t\t{x_cube:.2f}\t\t{M}\t{i+1}")

# ৪. সিমুলেটেড ইন্টিগ্রালের মান নির্ণয়
I_simulated = (M / N) * area_A

# ৫. Exact Area এবং Error হিসাব করা (বইয়ের পৃষ্ঠা ২১ অনুযায়ী)
exact_area = (5**4 / 4) - (2**4 / 4)  # প্রকৃত মান = 152.25
error = abs(exact_area - I_simulated)  # পরম ত্রুটি (Absolute Error)
percentage_error = (error / exact_area) * 100  # শতকরা ত্রুটি (Percentage Error)

print("-" * 72)
print(f"Total points under curve (M) = {M}")
print(f"Total trials (N)             = {N}")
print(
    f"Simulated Area (I)           = ({M}/{N}) * {area_A} = {I_simulated:.2f}"
)
print(f"Exact Area (Analytical)      = {exact_area:.2f}")
print(f"Absolute Error               = {error:.2f}")
print(f"Percentage Error             = {percentage_error:.2f}%")