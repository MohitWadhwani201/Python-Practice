from functools import wraps
# #decorators - functions that modify the behavior of other functions and enhance their functionality

# #decorators are denoted by @ symbol followed by the decorator name placed above the function to be decorated

# # def func1():
# #     print("this is function 1")

# # def func2():
# #     print("this is function 2")

# # func1()
# # func2()

# # #now if i want to add some extra functionality to func1 and func2 without modifying their code
# # #i can use decorators

# def decorator_function(any_function):
#     def wrapper_function():
#         print("this is extra functionality added to the function")
#         any_function()
#     return wrapper_function

# # a=decorator_function(func1) #decorating func1
# # a() #calling the decorated function

# # func2=decorator_function(func2)  #assigning the function with added functionality
# # func2() #calling the decorated function

# # #how to use @

# # @decorator_function   #shortcut to add functionality of decorator function
# # def func3():
# #     print('This is function 3')

# # func3()


# # to pass uncertain amount of arguments in our wrapper function we can use args and kwargs
# def decorator_function2(any_function):
#     @wraps(any_function)   #to preserve the original function's name and docstring
#     def wrapper_function(*args,**kwargs):
#         print(f"this is extra functionality added to the function with argument {args}")
#         return any_function(*args,**kwargs)              #so that it return the functions original return value
#     return wrapper_function

# @decorator_function2   #shortcut to add functionality of decorator function
# def func3(a):
#     print('This is function 3 ')

# func3(5)

# @decorator_function2
# def add(a,b):
#     return a+b

# print(add(5,6))
# print(add.__name__)  #prints the original function name because of @wraps
# print(add.__doc__)   #prints the original function docstring because of @wraps




#decorators pract


# def print_function_data(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         print(f"you are calling function {function.__name__}")
#         print(f"{function.__doc__}")
#         return function(*args,**kwargs)
#     return wrapper

# @print_function_data
# def add(a,b):
#     '''this function adds two numbers'''
#     return a+b

# print(add(5,6))


def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        for arg in args:
            if type(arg) is not int:
                print("only integers are allowed")
                return
        return function(*args,**kwargs)
    return wrapper

@only_int_allow
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add_all(1,2,3,4,5))