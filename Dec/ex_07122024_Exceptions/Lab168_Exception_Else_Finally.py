try:
    num1 = int(input("Enter a number 1 \n"))
    num2 = int(input("Enter a number 1 \n"))
    result = num1 / num2
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

else:
    print("Output is ", result)

finally:
    print("This code will be executed always!")
