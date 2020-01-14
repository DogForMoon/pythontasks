def solution(number):
    bef = []
    ans = 0
    number -= 1
    while number > 0:
        bef.append(number)
        number -= 1
    for i in bef:
        if i % 15 == 0:
            ans += i
            bef.remove(i)
        elif i % 5 == 0:
            ans += i
        elif i % 3 == 0:
            ans += i
    return ans

# https://www.codewars.com/kata/514b92a657cdc65150000006
