def factorial(n):
    answer = 1
    while n > 0:
        if n == 0:
            return 1
        else:
            answer *= n
            n -= 1
    return answer

# https://www.codewars.com/kata/57a049e253ba33ac5e000212
