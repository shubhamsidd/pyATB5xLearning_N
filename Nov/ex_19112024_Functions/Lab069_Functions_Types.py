# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / argument

import math

# 1. They can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")

greet()

# 2. # No Return Type and with Argument/ Param
def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Pramod")

# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="Pramod"):
    print("Hello", name.upper())


say_hello_default_arg("Dutta")
say_hello_default_arg()

def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, name2)

multiple_args()
multiple_args("Lucky", "Sharma")
multiple_args(name1="Pramod")
multiple_args(name1="Dutta", name2="Amit")
multiple_args(name2="Amit")