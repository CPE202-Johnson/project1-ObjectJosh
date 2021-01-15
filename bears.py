"""
If n is even, then you may give back n/2 bears.
If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
If n is divisible by 5, then you may give back 42 bears.
"""
# int to boolean
# Recursive function that figures out if reaching 42 bears is possible with the given rules, using permutations
def bears(n):
    """ Recursive function that figures out if reaching 42 bears is possible with the given rules, using permutations
    Args:
        n(int): number of starting bears
    Returns:
        bool: returned result of whether reaching 42 bears is possible with the given rules
    """
    if n == 42:
        return True
    if n < 42:
        return False
    reached_42 = False # if reached_42 is True, then don't go through any more "if" statements, work back up the recursion tree
    if n % 2 == 0 and not reached_42:
        if bears(n / 2):
            reached_42 = True
    if n % 3 == 0 or n % 4 == 0 and not reached_42:
        subtractor = n % 10 * ((n // 10) % 10)
        if subtractor != 0:
            if bears(n - subtractor):
                reached_42 = True
    if n % 5 == 0 and not reached_42:
        if bears(n - 42):
            reached_42 = True
    return reached_42 # returns True up the recursion tree if reached_42
