def even_or_odd(number):
    """
        Description: Accempts an integer as an input and judges whether it is odd or even.
        Output: "even" or "odd".
    
    """
    if type(number) == int:
        if number % 2 == 1:
            return "odd"
        else:
            return "even"
    else:
        return "Invalid input!"
    
    