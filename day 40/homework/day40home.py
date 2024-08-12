def bumps(road):                                                   #1
     return "Woohoo!" if road.count("n") <= 15 else "Car Dead"


def greet(name):                                                      #2
    a = (list(name))[0].upper() + ''.join((list(name))[1:]).lower()
    return "Hello {}".format(a) + "!"

def sum_even_numbers(seq):                                     #3
    # your code here
    nums = []
    b = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            nums.append(seq[i])
    for f in range(len(nums)):
        b = b + nums[f]
        
    return b



def reverse(lst):                                         #4
    empty_list = list()            
    result = list()
    while lst:
        result.append(lst.pop())
    return result
    

    

def averages(arr):                                      #5
    output = [] 
    try:        
        for i in range(len(arr)-1):
            output.append( (arr[i]+arr[i+1]) / 2 )        
        return output
    
    except:
        return output


def add(num1, num2):                             #6
    p, result = 1, 0
    while num1 or num2:
        current, num1, num2 = num1 % 10 + num2 % 10, num1 // 10, num2 // 10
        result += current * p
        p *= 10 if current < 10 else 100
    return result


def last_survivor(letters, coords):                   #7
    for i in coords:
        letters = letters[:i] + letters[i + 1:]
    return letters



def initialize_names(name):                      #8
    names = name.split()
    names[1:-1] = [n[0] + '.' for n in names[1:-1]]
    return ' '.join(names)

def get_issuer(number):                          #9     
    card = str(number)
    nums = len(card)
    
    if card[:2] in ("34", "37") and nums == 15:
        return "AMEX"
    elif card[:4] == "6011" and nums == 16:
        return "Discover"
    elif 51 <= int(card[:2]) <= 55 and nums == 16:
        return "Mastercard"
    elif card[0] == "4" and nums in (13, 16):
        return "VISA"
   

