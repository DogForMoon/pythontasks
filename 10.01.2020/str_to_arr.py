def string_to_array(args):
    a = list(args)
    answer = []
    word = ''
    for arg in args:
        if not arg == ' ':
            word += arg
        else:
            answer.append(word)
            word = ''
    answer.append(word)
    return answer
# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
