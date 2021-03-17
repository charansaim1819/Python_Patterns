#Shape of capital V:
def for_V():
    """printing capital 'V' using for loop"""
    for row in range(5):
        for col in range(9):
            if row-col==0 or row+col==8 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_V():
    """printing capital 'V' using while loop"""
    i=0
    while i<5:
        j=0
        while j<9:
            if i-j==0 or i+j==8:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
