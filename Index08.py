def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    f=s[4]
    if a=="*":
        return 0
    elif b=="*":
        return 1
    elif c=="*":
        return 2
    elif d=="*":
        return 3
    elif f=="*":
        return 4
    else:
        return False
print(main("salom"))
        