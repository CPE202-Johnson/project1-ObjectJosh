def convert(num, b):
    """ Recursive function that returns a string representing num in the base b
    Args:
        num(int): input number
        b(int): base number
    Returns:
        str: string representation of num in the base b
    """
    letter_list = ["A", "B", "C", "D", "E", "F", "G"]
    if num // b == 0:
        if num % b >= 10:
            return str(letter_list[num % b - 10]) # convert to alpha
        return str(num)
    base = num % b
    if num % b >= 10:
        base = letter_list[num % b - 10] # convert to alpha
    return str(convert(num // b, b)) + str(base)

if __name__ == "__main__":
    print(convert(16, 16))
    print(convert(160, 16))
    print(convert(0, 2))