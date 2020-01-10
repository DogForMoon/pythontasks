def sum_digits(number):
    numbers = list(str(number))
    answer = 0
    for i in numbers:
        if i.isdigit():
            answer += int(i)
    return answer
# https://www.codewars.com/kata/52f3149496de55aded000410
