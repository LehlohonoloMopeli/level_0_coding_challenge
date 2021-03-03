def vowels(word):
    """
    Description: Takes a string and returns the vowels in the string.
    type(output): str

    """
    if type(word) == str:
        vowels_list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

        letters_of_interest = []

        result = ""

        for letter in word:
            for element in vowels_list:
                if letter == element:
                    letters_of_interest.append(letter)

        if len(letters_of_interest) == 0:
            return None
        if len(letters_of_interest) > 0:
            for element in letters_of_interest:
                result += element
            return result

    else:
        return "Invalid input!"
