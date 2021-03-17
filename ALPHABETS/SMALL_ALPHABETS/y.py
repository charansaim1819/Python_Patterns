#Shape of small y:
def for_y():
    """printing small 'y' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==3 and row!=6 or col==0 and row in(0,1,2) or row==3 and col!=0 or row==6 and col in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_y():
    """printing small 'y' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==3 and i!=6 or j==0 and i in(0,1,2) or i==3 and j!=0 or i==6 and j in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
