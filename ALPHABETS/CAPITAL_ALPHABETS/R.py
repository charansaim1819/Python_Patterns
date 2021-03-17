#Shape of capital R:
def for_R():
    """printing capital 'R' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or row-col==3 or row==0 and col!=3 or col==3 and row in(1,2) or row==3 and col!=3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_R():
    """printing capital 'R' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 or i-j==3 or i==0 and j!=3 or j==3 and i in(1,2) or i==3 and j!=3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
