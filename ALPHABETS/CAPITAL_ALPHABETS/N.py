#Shape of capital N:
def for_N():
    """printing capital 'N' using for loop"""
    for row in range(5):
        for col in range(5):
            if col in(0,4) or row==col:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_N():
    """printing capital 'N' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j in(0,4) or i==j:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
