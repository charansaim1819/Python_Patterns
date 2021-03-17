#shape of capital P:
def for_P():
    """printing capital 'P' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or row in (0,3) and col!=3 or col==3 and row in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_P():
    """printing capital 'P' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 or i in(0,3) and j%3!=0 or j==3 and i in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
