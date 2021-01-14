"""
For each character in the input string:
    Form a simpler string by removing the character from the input string
    Generate all permutations of the simpler string recursively (i.e. call the perm_gen_lex function with the simpler string)
    Add the removed character to the front of each permutation of the simpler string, and add the resulting permutation to the list 
"""
def perm_gen_lex(a):
    """ Recursive function that generates all the permutations of the characters in a string
    Args:
        a(str): string being permutated
    Returns:
        perm_list(list): list of all the permutations of the input string 
    """
    if len(a) == 1:
        return [a]
    perm_list = []
    for i in range(len(a)):
        for each in perm_gen_lex(a[:i] + a[i + 1:]):
            perm_list.append(a[i] + each)
    return perm_list
