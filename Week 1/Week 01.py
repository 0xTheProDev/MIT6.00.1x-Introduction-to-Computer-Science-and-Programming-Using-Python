varA=raw_input("Enter varA : ")
varB=raw_input("Enter varB : ")

if(type(varA)==str or type(varB)==str):
    print 'string involved'
elif(varA>varB):
    print 'bigger'
elif(varA<varB):
    print 'smaller'
else:
    print 'equal'
