#Shape of small r:
def for_r():
    """printing small 'r' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==0 or row==0 and col!=2 or row==1 and col!=1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_r():
    """printing small 'r' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==0 or i==0 and j!=2 or i==1 and j!=1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
