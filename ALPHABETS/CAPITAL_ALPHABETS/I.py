#Shape of capital I:
def for_I():
    """printing capital 'I' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==2 or row in (0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_I():
    """printing capital 'I' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if i in(0,6) or j==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
