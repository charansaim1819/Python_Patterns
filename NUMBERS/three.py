#Shape of num 3:
def for_3():
    """printing number '3' using for loop"""
    for row in range(9):
        for col in range(4):
            if col in(0,1,2) and row%4==0 or col==3 and row%4!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_3():
    """printing number '3' using while loop"""
    i=0
    while i<9:
        j=0
        while j<4:
            if j in(0,1,2) and i%4==0 or j==3 and i%4!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

