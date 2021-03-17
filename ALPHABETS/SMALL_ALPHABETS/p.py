#Shape of small p:
def for_p():
    """printing small 'p' using for loop"""
    for row in range(8):
        for col in range(5):
            if col==1 or row==7 and col not in(3,4) or col in(2,3) and row in(1,4) or col==4 and row in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_p():
    """printing small 'p' using while loop"""
    i=0
    while i<9:
        j=0
        while j<5:
            if j==1 or i==8 and j in(0,2) or i in(1,4) and j in(2,3) or j==4 and i in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
