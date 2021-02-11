def convert_fahrenheit_to_celsius(fahrenheit):
    """
        Description: Accepts fahrenheit as an input and converts it to celsius.
        type(output) : float
    
    """
    if type(fahrenheit) == float or type(fahrenheit) == int:
        celsius = (5/9) * (fahrenheit - 32)
        return celsius 
    else:
        return "Invalid input!"
    
    
    
def convert_celsius_to_fahrenheit(celsius):
    """
        Description: Accepts celsius as an input and converts it to fahrenheit.
        type(output) : float
    
    """
    if type(celsius) == float or type(celsius) == int:
        fahrenheit = (celsius * (9/5)) + 32
        return fahrenheit
    else:
        return "Invalid Input!"