

print(55+45)
print(3*6+2)


n=2
print(n**2)


def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
 
a = 60
b = 48
 
# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcfnaive(60, 48))