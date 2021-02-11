from math import sqrt

def area_of_triangle(side1, side2, side3):
    """
        Description: Accepts the lengths of the sides of a triangle and calculates the area of the triangle.
        type(output) : float
    
    """
    try:
        if side1 > 0 and side2 > 0 and side3> 0:                   # Length cannot be negative
            semiparameter = (0.5) * (side1 + side2 + side3)        # semiparameter is equal to half the parameter of the triangle
            
            area = sqrt(semiparameter * (semiparameter - side1) * (semiparameter - side2)
                        * (semiparameter - side3))                 # Heron's formula
            return area
    
        else:
            return "Negative numbers not permitted!"
        
    except Exception as error:                                      # To handle unwanted inputs such as strings
        return "Invalid input!"

