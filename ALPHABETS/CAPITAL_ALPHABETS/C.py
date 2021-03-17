#Shape of capital C:
def for_C():
    """printing capital 'C' using for loop"""
    for row in range(6):
        for col in range(4):
            if col==0 and row not in(0,5) or row in(0,5) and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_C():
    """printing capital 'C' using while loop"""
    i=0
    while i<6:
        j=0 
        while j<4:
            if j==0 and  i not in(0,5) or i==0 and j!=0 or i==5 and j!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1

            
