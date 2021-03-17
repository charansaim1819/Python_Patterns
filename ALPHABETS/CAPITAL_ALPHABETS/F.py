#shape of capital F:
def for_F():
    """printing capital 'F' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0  or row in(0,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_F():
    """printing capital 'F' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i in(0,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1

