#Shape of capital Z:
def for_Z():
    """printing capital 'Z' using for loop"""
    for row in range(7):
        for col in range(7):
            if row+col==6 or row%6==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_Z():
    """printing capital 'Z' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i+j==4 or i in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
