#Shape of small d:
def for_d():
    """printing small 'd' using for loop"""
    for row in range(9):
        for col in range(6):
            if col==3 and row not in(8,8) or row==4 and col not in(0,4,5) or col==0 and row in(5,6,7) or row==8 and col in(1,2,4) or row==7 and col in(0,3,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_d():
    """printing small 'd' using while loop"""
    i=0
    while i<9:
        j=0
        while j<6:
            if j==3 and i not in(8,8) or i==4 and j not in(0,4,5) or j==0 and i in(5,6,7) or i==8 and j in(1,2,4) or i==7 and j in(0,3,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
