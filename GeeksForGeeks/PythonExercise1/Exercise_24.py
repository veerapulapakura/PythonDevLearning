#Program to find the information about functions.

print(str.__doc__)
print(sorted.__doc__)

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p Veera Pulapakura
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)