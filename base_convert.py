def convert(num, b):
    """ Recursive function that returns a string representing num in the base b
    Args:
        num(int): input number
        b(int): base number
    Returns:
        str: string representation of num in the base b
    """
    if num // b == 0:
        return str(num)
    base = num % b
    letter_list = ["A", "B", "C", "D", "E", "F", "G"]
    if num % b >= 10:
        base = letter_list[num % b - 10]
    return str(convert(num // b, b)) + str(base)
