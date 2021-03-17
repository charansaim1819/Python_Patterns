#Shape of small j:
def for_j():
    """printing small 'j' using for loop"""
    for row in range(8):
        for col in range(3):
            if col==2 and row!=1 or row==7 and col in(1,2) or row in(6,5) and col!=1 or row==2 and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_j():
    """printing small 'j' using while loop"""
    i=0
    while i<8:
        j=0
        while j<3:
            if j==2 and i!=1 or i==7 and j in(1,2) or i in(6,5) and j!=1 or i==2 and j!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
