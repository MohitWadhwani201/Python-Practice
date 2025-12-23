# def all_totals(*args):     #This *args can take any number of arguments and *args is of tuple type
#     total = 0
#     for arg in args:
#         if isinstance(arg, (int, float)):
#             total += arg
#         else:
#             raise ValueError(f"Invalid argument: {arg}")
#     return total


# def all_totals(a,b,*args):  # This *args can take any number of arguments and *args is of tuple type
#     total = a + b
#     for arg in args:
#         if isinstance(arg, (int, float)):
#             total += arg
#         else:
#             raise ValueError(f"Invalid argument: {arg}")
#     return total

# print(all_totals(1, 2) ) # Example usage