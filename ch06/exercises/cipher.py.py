def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A')
            if char.isupper(): 
                shift = 58
            else: 
                start = ord('a')
                shift = 61
            new_pos = (ord(char) - start + shift) % 26
            char = chr(start + new_pos)

        result += char
    
    return result

text = "The quick brown fox jumps over the lazy dog"
shift = 1
print("Text is : " + text)
# print("The shift pattern is : " + str(shift))
print("The cipher Text is : " + caesar_cipher(text, shift))

fptr = open("encrypted.txt", "w")
fptr.write(caesar_cipher(text, shift))
fptr.close()
