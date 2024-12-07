my_dict = {"name": "Shubham", "age": 26, "role": "SDET", "experience":3}
print(my_dict)

print(my_dict["age"])
my_dict["role"]="Manual Terster"
print(my_dict)

for key, value in my_dict.items():
    print(key,"--->", value)

    print("age" in my_dict)
    print("XYX" in my_dict)