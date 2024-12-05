cities = ("London", "Paris", "loss Angeles", "Tokyo")
print(cities)
print("Paris" in cities)
print("New Delhi" in cities)

t = (5,9,15)
print(type(t))
my_list = list(t)
print(type(my_list))
print(my_list)
my_list.append(18)
print(my_list)


ENV_API_URLS = tuple(["abc.com/get", "xyz.com/post", "qwe.com/put"])
print(ENV_API_URLS)