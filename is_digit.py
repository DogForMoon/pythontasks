def is_digit(n):
    if n.isdigit():
        if int(n) <= 9:
            return(True)
        else:
            return(False)
    else:
        return(False)
