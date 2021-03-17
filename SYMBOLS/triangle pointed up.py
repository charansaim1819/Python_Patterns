#Shape of triangle pointed up:
def for_triangle():
    """printing shape of 'triangle pointed up' using for loop"""
    for row in range(7):
        for col in range(9):
            if row==4 or row+col==4 or col-row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_triangle_up():
    """printing shape of 'triangle pointed up' using while loop"""
    i=0
    while i<7:
        j=0
        while j<9:
            if i==4 or i+j==4 or j-i==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1
    
