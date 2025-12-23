

# names = ["mohit", "sahil", "priyanshu"]
# print(min(names,key=lambda item: len(item))) #mohit
# print(max(names,key=lambda item: len(item))) #priyanshu

# key parameter takes a function as an argument and applies that function to each element in the iterable and returns the min/max based on the return value of that function

# students = [
#     {"name": "mohit", "age": 24},
#     {"name": "sahil", "age": 22},
#     {"name": "priyanshu", "age": 26},
# ]
# print(max(students, key=lambda item:item.get("age"))['name']) # priyanshu
# print(min(students, key=lambda item:item.get("age"))) # {'name': 'sahil', 'age': 22}


student={
    'mohit':{"age":24,"score":90},
    'sahil':{"age":22,"score":85},
    'priyanshu':{"age":26,"score":95},
}

print(max(student,key=lambda item:student[item]['score']))
# priyanshu
print(min(student,key=lambda item:student[item]['score']))
# sahil