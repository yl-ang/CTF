
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = "IOWJLQMAGH"
flag = ""
for character in encoded:
    flag+=letters[letters.index(character) % 26 - 18] #encode each character
    
print(flag)