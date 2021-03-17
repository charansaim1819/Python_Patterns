#Shape of capital U:
def for_U():
    """printing capital 'U' using for loop"""
    for row in range(7):
        for col in range(5):
            if col%4==0 and row%6!=0 or row==6 and col not in(0,4) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_U():
    """printing capital 'U' using while loop"""
    i=0
    while i<6:
        j=0
        while j<5:
            if j in (0,4) and i!=5 or i==5 and j not in (0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
