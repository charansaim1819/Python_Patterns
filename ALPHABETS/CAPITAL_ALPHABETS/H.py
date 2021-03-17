#Shape of capital H:
def for_H():
    """printing capital 'H' using for loop"""
    for row in range(7):
        for col in range(5):
            if col in(0,4) or row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_H():
    """printing capital 'H' using while loop"""
    i=0
    while i<7:
        j=0
        while j<6:
            if j in(0,5) or i==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
