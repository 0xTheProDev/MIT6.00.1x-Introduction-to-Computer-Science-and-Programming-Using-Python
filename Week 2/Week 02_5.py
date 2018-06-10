import math
def polysum(n,s):
    '''
    Return area and perimeter sq
    '''
    
    per=n*s
    num=0.25*n*s**2
    den=math.tan(math.pi/n)
    are=num/den
    s=are+per**2
    return round(s,4)
