# user_id=["user1","user2","user3"]
# names=["abc","bcd","cde"]
 
# #(''user1','abc'),('user2','bcd'),('user3','cde') zip function return an zip object which is an iterator of tuples

# print(zip(user_id,names)) #zip object
# print(list(zip(user_id,names))) #list of tuples
# print(tuple(zip(user_id,names))) #tuple of tuples

# you can iterate through the zip object only once but you can iterate through map object multiple times

# user_id=["user1","user2"]
# names=["abc","bcd","cde"]
 
# # smaller iterable is exhausted and the iteration stops
# print(list(zip(user_id,names))) #list of tuples

#if we have list of tuples we can convert it into dictionary using dict() function
# user_id=["user1","user2","user3"]
# names=["abc","bcd","cde"]
# print(dict(zip(user_id,names))) #dictionary

# but it will not work if there are duplicate keys or if there are more than 2 iterables

# user_id=["user1","user2","user3"]
# names=["abc","bcd","cde"]
# lastnames=["x","y","z"]
# # print(dict(zip(user_id,names,lastnames))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

# print(list(zip(user_id,names,lastnames))) #list of tuples


l1=[1,2,3]
l2=[3,4,5]
l = list(zip(l1,l2))
# print(l)

#how to unzip the zipped list

# zip(*l) #unzip the list of tuples
# # print(list(zip(*l)))
# li=list(zip(*l))
# l3=list(li[0]) #first list
# l4=list(li[1]) #second list
# print(l3)
# print(l4)

#---------OR----------

# l3,l4=zip(*l) #unzip the list of tuples
# print(list(l3)) #first list
# print(list(l4)) #second list

#practice question

# def average(*args):
#     average=[]
#     for values in zip(*args):
#         average.append(sum(values)/len(values))
#     return average
# print(average([1,2,3],[4,5,6],[7,8,9])) #[4.0, 5.0, 6.0]

# av=lambda *args: [sum(values)/len(values) for values in zip(*args)]
# print(av([1,2,3],[4,5,6],[7,8,9]))