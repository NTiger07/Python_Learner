string = input("Enter a sentence: ")
characters = []
spaces = []

for char in string:
    if char == " ":
        spaces.append(char)
    else:
        characters.append(char)
    
print(characters)
print(spaces)