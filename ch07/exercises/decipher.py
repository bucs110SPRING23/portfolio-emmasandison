def caesar_decipher(text, shift):
    result = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A')
            if char.isupper(): 
                shift = 24
            else: 
                start = ord('a')
                shift = 24
            new_pos = (ord(char) - start - shift) % 26
            char = chr(start + new_pos)

        result += char
    
    return result

text = "Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme"
shift = 1
print("Text is : " + text)
# print("The shift pattern is : " + str(shift))
print("The decrypted cipher Text is : " + caesar_decipher(text, shift))

fptr = open("decrypted.txt", "w")
fptr.write(caesar_decipher(text, shift))
fptr.close()