#Shape of small h:
def for_h():
    """printing small 'h' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or row==3 and col in(1,2) or col==3 and row in(4,5,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_h():
    """printing small 'h' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 or i==3 and j not in(3,3) or j==3 and i in (4,5,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
