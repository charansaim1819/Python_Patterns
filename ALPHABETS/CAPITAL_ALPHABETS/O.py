#Shape of capital O:
def for_O():
    """printing capital 'O' using for loop"""
    for row in range(6):
        for col in range(6):
            if row%5==0 and col%5!=0 or col%5==0 and row%5!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_O():
    """printing capital 'O' using while loop"""
    i=0
    while i<6:
        j=0
        while j<6:
            if i%5==0 and j%5!=0 or j%5==0 and i%5!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
