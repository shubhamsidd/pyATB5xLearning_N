# Method Overloading is Not Supported - Python

class calc:

    def sum(selfa, a, b):
        return a+b

    def sum(self, a, b, c):
        return  a+b+c

calc_ref = calc()
result = calc_ref.sum(3,4)
print(result)
