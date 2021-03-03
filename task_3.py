def hello(name):
    """
        Description: Accepts the name of an individual and prints "Hello ..." where
            the ellipsis represents the name of the individual.
        type(output) : str 
    
    """
    if type(name) == str:
        result = print("Hello " + name + "!")
        return result
    else:
        return "Invalid input!"
