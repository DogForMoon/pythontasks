def how_much_i_love_you(nb_petals):
    a = nb_petals % 6
    if a == 1:
        return 'I love you'
    elif a == 2:
        return 'a little'
    elif a == 3:
        return 'a lot'
    elif a == 4:
        return 'passionately'
    elif a == 5:
        return 'madly'
    elif a == 0:
        return 'not at all'
#https://www.codewars.com/kata/57f24e6a18e9fad8eb000296