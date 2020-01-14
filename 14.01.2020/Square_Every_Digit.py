def square_digits(num):
    squr = list(str(num))
    answer = ''
    for i in squr:
        answer += str(int(i) ** 2)
    return int(answer)

# https://www.codewars.com/kata/546e2562b03326a88e000020