t= tuple()
print(type(t))

# Conversion List to Tuple
t1 = tuple(["shubham", "amit", "mansha"])
print(t1)
print(type(t1))

hero1 = ("Batman", "Bruce wayne")
hero2 = ("wonder woman", "Diana Prince")
new_tuple = (hero1, hero2)
print(new_tuple)
print(new_tuple[0])  # ("Batman", "Bruce Wayne")
print(new_tuple[0][0]) # "Batman"
print(new_tuple[1][1])