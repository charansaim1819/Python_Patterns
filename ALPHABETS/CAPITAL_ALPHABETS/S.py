#Shape of capital S:
def for_S():
    """printing capital 'S' using for loop"""
    for row in range(9):
        for col in range(4):
            if col==0 and row in(1,2,5) or col in(1,2) and row in(0,3,6)  or col==3 and row in(1,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_S():
    """printing capital 'S' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 and i in(1,2,5) or j in(1,2) and i in(0,3,6)  or j==3 and i in(1,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
