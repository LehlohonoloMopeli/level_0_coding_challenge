from math import sqrt


def area_of_triangle(side1, side2, side3):
    """
    Description: Accepts the lengths of the sides of a triangle and calculates the area of the triangle.
    input: positive float
    type(output) : float

    """

    try:
        if side1 > 0 and side2 > 0 and side3 > 0:
            semiparameter = (0.5) * (side1 + side2 + side3)

            area = sqrt(
                semiparameter
                * (semiparameter - side1)
                * (semiparameter - side2)
                * (semiparameter - side3)
            )                                                   # Heron's formula
            return area

        else:
            return "Negative numbers not permitted!"
    except:
        return "Invalid input!"
