from math import sqrt

def area_of_triangle(side1, side2, side3):
    """
        Description: Accepts the lengths of the sides of a triangle and calculates the area of the triangle.
        type(output) : float
    
    """
    if side1 > 0 and side2 > 0 and side3> 0:
        semiparameter = (0.5) * (side1 + side2 + side3)        # semiparameter is equal to half the parameter of the triangle
        
        area = sqrt(semiparameter * (semiparameter - side1) * (semiparameter - side2)
                    * (semiparameter - side3))                 # Heron's formula
    
        return area
    
    else:
        return "Not a valid input!"
