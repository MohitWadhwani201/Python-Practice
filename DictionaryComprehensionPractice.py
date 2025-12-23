# square={i:i**2 for i in range(1,11)}
# print(square)

# square={f"Square of {i} is":i**2 for i in range(1,11)}
# print(square)

string = "Hello World"
word_count={char:string.count(char) for char in string if char != " "}
print(word_count)