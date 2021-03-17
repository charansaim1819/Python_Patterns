#Shape of capital Q:
def for_Q():
    """printing capital 'Q' using for loop"""
    for row in range(6):
        for col in range(7):
            if col%5==0 and row%5!=0 or row in(0,5) and col not in(0,5,6) or row==3 and col==4  or row==5 and col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_Q():
    """printing capital 'Q' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==0 and i not in (0,4) or j==1 and i in(0,4) or j==2 and i not in(1,3) or j==3 and i not in(0,4) or i==4 and j not in(0,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
