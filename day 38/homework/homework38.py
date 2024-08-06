def filter_list(l):                                           #1
    'return a new list with the strings filtered out'
    new_list =[]
    for x in l:
        if type(x) != str:
            new_list.append(x)
    return new_list



def sum_two_smallest_numbers(numbers):              #2
    #your code here
    smallest1 = None
    smallest2 = None 
    for n in numbers: 
        if not smallest1 or n < smallest1: 
            smallest2 = smallest1
            smallest1 = n 
        elif not smallest2 or n < smallest2: 
            smallest2 = n 
    return smallest1 + smallest2


def solution(text, ending):                      #3
    # your code here...
    text1 = len(text) - len(ending)
    text2 = len(text) - text1
    text3 = text[text1:]
    if text3 == ending:
        return True
    else:
        return False
        

def stray(arr):                          #4
    if arr[0] == arr[1]:
        for x in arr:
            if x != arr[0]:
                return x
    if arr[0] == arr[2]:
        return arr[1]
    return arr[0]