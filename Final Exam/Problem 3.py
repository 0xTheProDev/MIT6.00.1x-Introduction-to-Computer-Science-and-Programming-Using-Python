trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num)
    string = ''
    def map_to_mandarin(key):
        return trans[str(key)]
    if(num <= 10):
        string = map_to_mandarin(num)
    elif(num < 20):
        string = map_to_mandarin(10)
        if(num % 10 != 0):
            string += ' ' + map_to_mandarin(num % 10)
    else:
        string = map_to_mandarin(num // 10) + ' ' + map_to_mandarin(10)
        if(num % 10 != 0):
            string += ' ' + map_to_mandarin(num % 10)
    return string

print(convert_to_mandarin('36'))
