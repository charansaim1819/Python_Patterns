#Shape of capital Y:
def for_Y():
    """printing capital 'Y' using for loop"""
    for row in range(6):
        for col in range(7):
            if row==0 and col in(0,6) or row==1 and col in(1,5) or row==2 and col in(2,4) or col==3 and row not in(0,1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_Y():
    """printing capital 'Y' using while loop"""
    i=0
    while i<6:
        j=0
        while j<7:
            if j in(0,6) and i==0 or j in (1,5) and i==1 or j in (2,4) and i==2 or j==3 and i in(3,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
