def two_sort(array):
    ends = []
    word = ''
    array.sort()
    stars = list(array[0])
    end_letter = stars.pop(-1)
    for star in stars:
        star += '***'
        ends.append(star)
    for end in ends:
        word += end
    return word + end_letter
#https://www.codewars.com/kata/57cfdf34902f6ba3d300001e