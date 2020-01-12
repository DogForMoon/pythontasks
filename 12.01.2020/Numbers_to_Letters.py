import string


def switcher(arrs):
    alphabet = {}
    n = 26
    alphs = list(string.ascii_lowercase)
    for alph in alphs:
        alphabet[str(n)] = alph
        n -= 1
    alphabet['27'] = '!'
    alphabet['28'] = '?'
    alphabet['29'] = ' '

    answer = ''

    for arr in arrs:
        answer += alphabet.get(arr)
    return answer

# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c
