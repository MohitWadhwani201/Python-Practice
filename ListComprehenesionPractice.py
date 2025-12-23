# square2=[-i for i in range(1,10)]
# # print(square2)

# newlist=[i**2 for i in square2]
# print(newlist)

# square2=['abc', 'def', 'ghi', 'jkl']


# newlist=[ name[::-1] for name in square2 ]
# print(newlist)

# square2=[-i for i in range(1,11)]
# # # print(square2)

# newlist=[i**2 for i in square2 if i%2==0]
# print(newlist)

# square2=[True, False, [1,2,3],{'key': 'value'}, 42, None,101,1.1]
# # # print(square2)

# newlist=[i for i in square2 if type(i) is int or type(i) is float]
# print(newlist)

square2=[-i for i in range(1,11)]
# # print(square2)

newlist=[i**2 if  i%2==0 else i**3 for i in square2 ]
print(newlist)