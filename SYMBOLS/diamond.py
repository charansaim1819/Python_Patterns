#Shape of diamond:
def for_daimond():
    """printing  shape of'diamond' using for loop"""
    for row in range(7):
        for col in range(7):
            if row+col==3 or row-col==-3 or row-col==3 or row+col==9:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_diamond():
    """printing  shape of'diamond' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if i+j==3 or i-j==-3 or i-j==3 or i+j==9:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
