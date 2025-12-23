numbers=[9,3,6,7,1]

# print(all(num%2==0 for num in numbers) )#True
# all function returns True if all the elements in the iterable are true otherwise it returns False

# print(any(num%2==0 for num in numbers) )#True

# any function returns True if any of the elements in the iterable is true otherwise it returns False


def total(*args):
    if(all([(type(arg)==int or type(arg)==float)for arg in args])):
        return sum(args)
    else:
        return "All arguments must be numbers"
    
print(total(1,2,3,4,"5")) #6