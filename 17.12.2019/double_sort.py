def db_sort(arrs):
    digit = []
    string = []
    for arr in arrs:
        if isinstance(arr, int):
            digit.append(arr)
        elif isinstance(arr, str):
            string.append(arr)
    digit.sort()
    string.sort()
    return(digit + string)
    #https://www.codewars.com/kata/57cc79ec484cf991c900018d