def vowels(word):
    """
        Description: Takes a string and returns the vowels in the string.
        type(output): str
    
    """
    if type(word) == str:
        vowelsList = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        
        lettersOfInterest = []
        
        result = ""
        
        for letter in word:
            for element in vowelsList:
                if letter == element:
                    lettersOfInterest.append(letter)
        
        if len(lettersOfInterest) == 0:
            return None
        if len(lettersOfInterest) > 0:
            for element in lettersOfInterest:
                result += element 
            return result
    
    else:
        return "Invalid input!"
