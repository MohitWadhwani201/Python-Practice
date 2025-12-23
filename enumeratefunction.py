# how to tract position without using enumerate function
# names = ["abc","bcd","cde","def"]
# position = 0
# for name in names:
#     print(f"{position} : {name}")
#     position += 1

# # using enumerate function
# for pos,name in enumerate(names):
#     print(f"{pos} : {name}")

def findstring(s,l):
    for pos, name in enumerate(l):
        if name == s:
            return pos
    return -1

l=["abc","bcd","cde","def"]
print(findstring("obc",l))  

