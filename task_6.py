def get_maximum(num1, num2, num3):
    """
    Description: Accepts three numbers and returs their maximum.
    input: float
    type(output) : float

    """

    try:
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        elif num3 >= num1 and num3 >= num2:
            return num3

    except:
        return "Invalid input!"
