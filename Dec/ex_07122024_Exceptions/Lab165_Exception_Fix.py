from sys import exception

print("----Start of the Program")
try:

    a = int(input("Enter the num1 "))
    b = int(input("Enter the num2 "))
    c = a / b # ZeroDivisionError: division by zero
    print("Division result is ", c)
except Exception as e:
    print(e)

print("----End of Program")


# try and Except