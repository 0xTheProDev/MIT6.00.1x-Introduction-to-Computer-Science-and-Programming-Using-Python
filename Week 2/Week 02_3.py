def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    s = lo + x + hi
    s -= (max(lo,hi,x) + min(lo,hi,x))
    return round(s,2)
