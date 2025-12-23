# numbers=[1, 2, 3, 4, 5]
# def square(n):
#     return n**2

# print(map(square,numbers)) #prints the map object
# print(list(map(square,numbers))) #prints the list of squared numbers

#using lambda function
numbers=[1, 2, 3, 4, 5]
def square(n):
    return n**2

print(map(lambda a : a**2,numbers)) 
print(list(map(lambda a : a**2,numbers)))