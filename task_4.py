def even_or_odd(number):
    """
        Description: Accempts an integer as an input and judges whether it is odd or even.
        Output: "even" or "odd".
    
    """
    if number % 2 == 1:
        return "odd"
    elif number % 2 == 0:
        return "even"
    else:
        return "Not a valid input!"
    