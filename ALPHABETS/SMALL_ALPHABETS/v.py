#shape of small v:
def for_v():
    """printing small 'v' using for loop"""
    for row in range(4):
        for col in range(7):
            if row==col or row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_v():
    """printing small 'v' using while loop"""
    i=0
    while i<4:
        j=0
        while j<7:
            if i==j or i+j==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
