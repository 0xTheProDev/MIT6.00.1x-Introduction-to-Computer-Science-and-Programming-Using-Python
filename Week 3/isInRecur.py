def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    n = len(aStr)
    if(n == 0):
        return False
    c = aStr[n/2]
    if(c == char):
        return True
    elif(c > char):
        return isIn(char, aStr[:n/2])
    else:
        return isIn(char, aStr[n/2:])
