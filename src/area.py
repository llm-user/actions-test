def calculate_area_square(length: int | float) -> int | float:
    """
    Function to calculate the area of a square
    :param length: length of the square
    :return: area of the square
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length

def calculate_volume(length: int) -> int:
    if not isinstance(length, int):
        raise TypeError("Length must be an integer")
    elif length <=0:
        raise ValueError("Length must be positive")
    else:
        return length**3
