def x_y_input():
    """
       function that get from the user x,y input

       Returns: x: int, y: int
   """
    try:
        x, y = input("Enter x,y coordinates between 1-100 (e.g. 2,2)\n").split(',')
    except TypeError:
        raise TypeError("Error: invalid format, the arguments must be comma separated. ")
    validate_drone_input_x_y(x, y)
    return int(x), int(y)


def validate_drone_input_x_y(x: str, y: str):
    """
       function that validate the x,y input

       Args: x: int, y: int
    """
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError("Error: x,y must be integers.")
    if int(x) < 0 or int(x) > 100 or int(y) < 0 or int(y) > 100:
        raise ValueError("Error: x,y values to be between 0-100 included. ")
