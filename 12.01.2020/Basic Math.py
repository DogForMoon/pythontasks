def calculate(s):
    exps = list(s)
    reply = 0
    temp = ''
    for exp in exps:
        if exp == 'p':
            reply += int(temp)
            temp = ''
        elif exp == 'm':
            reply += int(temp)
            temp = ''
            temp += '-'
        elif exp.isdigit():
            temp += exp
    reply += int(temp)
    return str(reply)

# https://www.codewars.com/kata/5809b62808ad92e31b000031
