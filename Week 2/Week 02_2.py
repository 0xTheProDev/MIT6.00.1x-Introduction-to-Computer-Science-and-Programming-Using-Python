# Paste your code into this box
maxnum = 100
minnum = 0
print "Please think of a number between 0 and 100!"
c = '0'
while c!='c':
    g=(maxnum+minnum)/2
    print("Is your secret number "+str(g)+"?")
    c = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if c=='h':
        maxnum=g
    elif c=='l':
        minnum=g
    else:
        if c!='c':
            print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: "+str(g))
