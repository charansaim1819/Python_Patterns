#Shape of small t:
def for_t():
    """printing small 't' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==1 or row==3 and col!=3 or row==6 and col==2 or row==5 and col==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_t():
    """printing small 't' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==1 or i==3 and j!=3 or j==2 and i in(3,6) or j==3 and i==5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
