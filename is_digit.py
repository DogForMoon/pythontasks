def is_digit(n):
    if n.isdigit():
        if int(n) <= 9:
            return(True)
        else:
            return(False)
    else:
        return(False)
#https://www.codewars.com/kata/567bf4f7ee34510f69000032