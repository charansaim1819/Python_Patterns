#Shape of small z:
def for_z():
    """printing small 'z' using for loop"""
    for row in range(5):
        for col in range(5):
            if row in(0,4) or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_z():
    """printing small 'z' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if i+j==4 or i in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
