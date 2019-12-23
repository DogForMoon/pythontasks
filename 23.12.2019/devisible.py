def is_divisible(n, x, y):
    if n % x == 0:
        if n % y == 0:
            return True
        else:
            return False
    else:
        return False
#https://www.codewars.com/kata/5545f109004975ea66000086