# Problem to find the max between two.

# Logic Building Formula

# 1 . user inputs -> two integers
# 2. o/ p ->  int 1 which ever is grater max number it will return.
# 31.4 or 45.34 - float

num1 = float(input("Enter the first value\n"))
num2 = float(input("Enter the second value\n"))

if num1 >= num2:
    print("max is num1 ->", num1)
else:
    print("max is num2 ->", num2)

# Edge Cases - num1 == num2 ->  Handled.
# String -> ABC, ten -> try and except - We will learn this in future.
# -ve Value -> We will learn this in future.