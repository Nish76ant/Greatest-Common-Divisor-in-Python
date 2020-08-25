def gretestNumberDivisor(a,b):

    if a == b:
        return a

    elif a%b == 0:
        return b

    elif b%a  == 0:
        return a

    elif a>b:
        return gretestNumberDivisor(a%b,b)
    else:
        return gretestNumberDivisor(a,b%a)

print('Greatest Common divisor of these numbers is',gretestNumberDivisor(105,91))
