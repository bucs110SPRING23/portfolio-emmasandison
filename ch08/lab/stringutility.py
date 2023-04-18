# Part A
class StringUtility: 
    def __init__(self, string): 
        self.string = string 

    def __str__(self): 
        """
        This method returns the string that was defined in the 'init' method
        """
        return self.string 
    
    def vowels(self):
        vowels = sum([1 for char in self.string if char.lower() in 'aeiou'])
        if vowels < 5: 
            return str(vowels)
        else: 
            return "many"
    
    def bothEnds(self): 
        if len(self.string) <= 2: 
            empty = ""
            return empty
        else: 
            return self.string[:2] + self.string[-2:]
        
    def fixStart(self): 
        if len(self.string) <= 1:
            return self.string 
        else: 
            char = self.string[0]
            str = self.string 
            str = str.replace(char, "*")
            str = char + str[1:]
            return str 
    
    def asciiSum(self): 
        str = self.string 
        integer = sum(ord(char) for char in str)
        return integer 
    
    def cipher(self):
        result = ""
        for char in self.string:
            if char.isalpha():
            
                if char.isupper():
                    start = ord('A')
                    wrap = 26
                else:
                    start = ord('a')
                    wrap = 26
                
                char_ord = ord(char)
                new_pos = ((char_ord - start + len(self.string)) % wrap) + start
            
                result += chr(new_pos)
            else:
                result += char
    
        return result

            
