# tuples strings lists are iterable
# iterables can be used in for loops
# iterables can be converted to iterators using iter() function
# iterators are objects which can be iterated upon

# for i in [1,2,3,4,5]:
#     print(i)

# a=iter([1,2,3,4,5])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a)) #StopIteration error

numbers=[1,2,3,4,5]
squares=map(lambda a : a**2,numbers) #map object is an iterator

print(next(squares))
print(next(squares))

# next(numbers) #TypeError: 'list' object is not an iterator

# iterables are those which can be converted to iterators