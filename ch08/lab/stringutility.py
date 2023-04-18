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
        count = 0
        vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        for char in self.string: 
            if char in vowels:
                count += 1
        if count >= 5: 
            return "many"
        return str(count)
    
    def bothEnds(self): 
        if len(self.string) <= 2: 
            empty = ""
            return empty
        else: 
            return self.string[0:1] + self.string[-2:-1]
        
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
        
        

        
    
        
        

        

        
    

