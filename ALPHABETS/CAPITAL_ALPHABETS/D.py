#Shape of capital D:
def for_D():
    """printing  capital 'D' using for loop"""
    for row in range(5):
        for col in range(5):
            if col==1 or row in(0,4) and col!=4 or col==4 and row not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_D():
    """printing  capital 'D' using while loop"""
    i=0
    while i<4:
        j=0
        while j<5:
            if i==0 and j!=4 or i==3 and j!=4 or j==1 or j==4 and i not in(0,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1

