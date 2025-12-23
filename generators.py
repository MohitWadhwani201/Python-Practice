#generators are iterators, but with a different approach

#iterable are objects that can be iterated over, like lists, tuples, and strings
#iterator are objects that can be iterated upon, meaning that you can traverse through all the values
# iterables are converted to iterators using the iter() function by python internally

# l=[1,2]

# i=iter(l)  #converts the list to an iterator object

# print(next(i))  #gives the next value in the iterator
# print(next(i))
# print(next(i))  #gives error because there are no more elements in the iterator

# i= map(lambda x:x*2, [1,2,3])  #map returns an iterator that applies the function to each item of the iterable
# print(next(i))   #works as map returns an iterator

# we use generators instead of iterators as they are easier to implement and use less memory
# generators only produce one value at a time and only when required, instead of storing all the values in memory
# they are best suited for when you want to iterate once over a large dataset

# def nums(n):
#      for i in range(n):
#          yield i*2   #yield is used to produce a value and pause the function, maintaining its state for next call
#             #when the function is called again, it resumes from where it left off
#             #yield is used in place of return to make a function a generator

# # for i in nums(10):
# #     print(i)

# num = nums(10)  #creates a generator object

# # for i in range(11):
# #     print(next(num))  #gets the next value from the generator

# # for i in range(11):
# #     print(next(num))  #gives error as the generator is exhausted after the first loop

# #how to convert generator to a list

# print(list(nums(10)))  #converts the generator to a list by iterating through all its values
# # but this is not memory efficient as it stores all values in memory

#practice

# def even(n):
#     for i in range(int((n/2)+1)):
#         yield i*2

# for i in even(9):
#     print(i)

#generator comprehension
#similar to list comprehension but with parentheses instead of square brackets

# gen = (i*2 for i in range(10))  #creates a generator object

# for i in gen:
#     print(i)

# for i in gen:
#     print(i)  #gives error as the generator is exhausted after the first

#list vs generator
# l=[i**2 for i in range(10000000)]  #creates a list and stores all values in memory
# print(l)
# gen = (i*2 for i in range(10000000))  #creates a generator object that produces values on the fly

