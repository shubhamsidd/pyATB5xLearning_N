student_infor1 = {
    "name": "Pramod",
    # "age": 65,
    "age": 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_infor2 = {
    "name": "Amit",
    # "age": 65,
    "age": 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_infor3 = {
    "name": "Murthy",
    # "age": 65,
    "age": 120,
    "address": {
        "home_address": "PODI",
        "office_address": "vizag"
    }
}

my_list = [student_infor1, student_infor2, student_infor3]
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[2]['address'])
print(my_list[2]['address']['office_address'])

#Alternate way
#
print(student_infor3["address"]["office_address"])