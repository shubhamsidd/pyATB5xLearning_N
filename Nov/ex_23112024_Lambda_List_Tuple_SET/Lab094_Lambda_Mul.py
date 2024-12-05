 #Write a program to calcuclate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

num = int(input("Enter the number\n"))

result = lambda num: "Even" if num % 2 == 0 else "odd"
# find_even_odd(5)
print(result(num))