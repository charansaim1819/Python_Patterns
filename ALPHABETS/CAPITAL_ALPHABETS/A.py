#Shape of capital A:
def for_A():
    """printing capital 'A' using for loop"""
    for row in range(6):
        for col in range(11):
            if row+col == 5 or col-row==5 or row==3 and col not in(0,1,9,10):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_A():
    """ printing capital 'A' using while loop"""
    row=0
    while row<6:
        col=0
        while col<11:
            if col+row==5 or col-row==5 or row==3 and col not in(0,1,9,10):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        print()
        row+=1

