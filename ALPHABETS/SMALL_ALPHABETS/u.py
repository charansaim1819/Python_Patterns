#Shape of small u:
def for_u():
    """printing small 'u' using for loop"""
    for row in range(5):
        for col in range(5):
            if col==3 and row!=4 or row==4 and col not in(0,3) or col==0 and row!=4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


def while_u():
    """printing small 'u' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j==3 and i!=4 or i==4 and j not in(0,3) or j==0 and i!=4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
