#Shape of small q:
def for_q():
    """printing small 'q' using for loop"""
    for row in range(9):
        for col in range(5):
            if row==8 and col not in(0,1) or col==3 or col in(1,2) and row in(1,4) or col==0 and row  in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_q():
    """printing small 'q' using while loop"""
    i=0
    while i<9:
        j=0
        while j<5:
            if j==3 or i==8 and j in(2,4) or j in(1,2) and i in(1,4) or j==0 and i in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
