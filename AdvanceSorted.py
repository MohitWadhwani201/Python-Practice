# fruits=['banana','apple','mango','kiwi','orange']
# fruits.sort()
# print(fruits)

# fruits2=('banana','apple','mango','kiwi','orange') #tuple cannot be sorted using sort method because they are immutable
# # fruits2.sort() #AttributeError: 'tuple' object has no attribute 'sort'

# sorted_fruits=sorted(fruits2) #sorted function returns a new sorted list from the elements of any iterable
# print(sorted_fruits)

# fruits3={'banana','apple','mango','kiwi','orange'} #set cannot be sorted using sort method because they are unordered
# sorted_fruits3=sorted(fruits3) #sorted function returns a new sorted list from the elements of any iterable
# print(sorted_fruits3)

guitars=[
    {'model':'yamaha f310','price':8400},
    {'model':'faith naptune','price':5000},
    {'model':'taylor 814ce','price':45000},
    {'model':'taylor gs mini','price':20000},
    {'model':'faith apollo','price':35000},
]

# guitars.sort(key=lambda item:item['price'])
# # print(guitars)
# print(sorted(guitars,key=lambda item:item['price'],reverse=True)) #sorted in descending order
# guitar = {
#     'yamaha f310': {'name': 'yamaha', 'price': 8400},
#     'faith naptune': {'name': 'faith', 'price': 5000},
#     'taylor 814ce': {'name': 'taylor', 'price': 45000},
#     'taylor gs mini': {'name': 'taylor', 'price': 20000},
#     'faith apollo': {'name': 'faith', 'price': 35000},
# }

# print(sorted(guitar,key=lambda item:guitar[item]['price']))

#extra features of functions

# def add(a,b):
#     '''this adds two numbers'''
#     return a+b
# print(add.__doc__) # prints the discription mentioned in '''_____''' space

# print(len.__doc__)

print(help(sorted)) #prints the discription of the function and its parameters