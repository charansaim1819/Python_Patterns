#Shape of small k:
def for_k():
    """printing small 'k' using for loop"""
    for row in range(5):
        for col in range(4):
            if col==0 or row-col==1 or row==1 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_k():
    """printing small 'k' using while loop"""
    i=0
    while i<6:
        j=0
        while j<4:
            if j==0 or i-j==2 or i==2 and j not in(1,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
