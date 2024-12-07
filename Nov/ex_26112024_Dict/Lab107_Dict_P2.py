student_infor = {
    "name": "Pramod",
     #"age": 65,
    "age": 67,
    "address": "KA"
}
print(student_infor)

print(student_infor["name"])
print(student_infor["age"])
print(student_infor["address"])
student_infor["age"] = 26
print(student_infor)

student_infor2 = dict(name="Pramod", age=67, address="KA")


student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}


print((student_infor1))

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

print(student_infor2)


#for (key,value) in student_infor.items():
   # print(key,"-->",value)

