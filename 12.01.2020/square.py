import math


def is_square(n):
    try:
        i = math.sqrt(n)
        answer = i % 1
        if answer == 0:
            return True
        else:
            return False
    except ValueError:
        return False

# https://www.codewars.com/kata/54c27a33fb7da0db0100040e
