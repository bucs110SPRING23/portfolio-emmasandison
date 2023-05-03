
class StringUtility: 
    """
    This class consists of several methods that take a string and alters it differently within each method
    """
    def __init__(self, string): 
        self.string = string 

    def __str__(self): 
        """
        This method returns the original string unchanged
        """
        return self.string 
    
    def vowels(self):
        """
        This method returns the number of vowels as a string
        If the number of vowels is greater than or equal to 5, the word 'many" is returned instead
        """
        vowels = sum([1 for char in self.string if char.lower() in 'aeiou'])
        if vowels < 5: 
            return str(vowels)
        else: 
            return "many"
    
    def bothEnds(self): 
        """
        This method returns a string with the first 2 and last 2 characters of the original string
        If the string is less than or equal to 2, it returns an empty string instead
        """
        if len(self.string) <= 2: 
            empty = ""
            return empty
        else: 
            return self.string[:2] + self.string[-2:]
        
    def fixStart(self): 
        """
        This method returns a string where the all occurences of the first character has been changed to '*', the first character isn't changed
        If the string is less than or equal to 1, just the parameter is returned
        """
        if len(self.string) <= 1:
            return self.string 
        else: 
            char = self.string[0]
            str = self.string 
            str = str.replace(char, "*")
            str = char + str[1:]
            return str 
    
    def asciiSum(self): 
        """
        This methods returns an integer that is the sum of all ascii values in the string
        """
        str = self.string 
        integer = sum(ord(char) for char in str)
        return integer 
    
    def cipher(self):
        """
        This method returns an encoded string by shifting each letter by the length of the string
        Any characters that are not letters are left unchanged
        """
        result = ""
        for char in self.string:
            if char.isalpha():
            
                if char.isupper():
                    start = ord('A')
                else:
                    start = ord('a')
                
                char_ord = ord(char)
                shift = len(self.string)
                new_pos = ((char_ord - start + shift) % 26) + start
            
                result += chr(new_pos)
            else:
                result += char
    
        return result

            
