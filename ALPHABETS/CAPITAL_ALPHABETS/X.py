#Shape of capital X:
def for_X():
    """printing capital 'X' using for loop"""
    for row in range(7):
        for col in range(7):
            if row-col==0 or row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_X():
    """printing capital 'X' using while loop"""
    i=0
    while i<6:
        j=0
        while j<6:
            if i-j==0 or i+j==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
