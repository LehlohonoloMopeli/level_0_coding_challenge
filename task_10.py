def common_characters(string1, string2):
    """
    Description: Takes two words as argumnts and returns the common leters between them.
    type(output): str

    """
    try:
        commonLetters = []

        result = ""

        for letter in string1:
            for element in string2:
                if letter == element and letter not in commonLetters:
                    commonLetters.append(letter)

        if len(commonLetters) == 0:
            return "Common letters: " + str(None)

        elif len(commonLetters) == 1:
            for element in commonLetters:
                result += str(element)
            return "Common letters: " + result

        elif len(commonLetters) > 1:
            result += str(commonLetters[0])
            for element in commonLetters[1:]:
                result += ", " + str(element)
            return "Common letters: " + result

    except:
        return "Invalid input!"
