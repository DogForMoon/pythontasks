def draw_stairs(n):
    answer = ''
    stairs = ['I\n'] * (n - 1)
    stairs.append('I')
    b = 0
    for stair in stairs:
        if b <= n:
            answer += ' ' * b + stair
            b += 1
        else:
            pass
    return answer
#https://www.codewars.com/kata/5b4e779c578c6a898e0005c5