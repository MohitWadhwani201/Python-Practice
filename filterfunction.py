def iseven(n):
    return n%2==0

numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens=filter(iseven,numbers) #prints the filter object
# print(evens)

# print(list(evens)) #prints the list of even numbers
# print(tuple(evens)) #prints the tuple of even numbers

evens=filter(lambda a : a%2==0,numbers) #prints the filter object
print(list(evens))

#you can iterate through the filter object only once but you can iterate through map object multiple times