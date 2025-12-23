# def my_map(func,l):
#     result = []
#     for i in l:
#         result.append(func(i))
#     return result

# def square(x):
#     return x*x

# print(my_map(lambda a:a**2,[1,2,3,4,5]))

#returning function from another function (closure/first class function)

# def outer_func():
#     def inner_func():
#         print("this is inner function")
#     return inner_func

# a=outer_func()
# a()

# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power


# cube = to_power(3)
# square = to_power(2)
# quad = to_power(4)

# print(cube(3))
# print(square(3))
# print(quad(3))
