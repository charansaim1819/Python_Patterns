#Shape of square:
def for_square():
    """printing  shape of'square' using for loop"""
    for row in range(7):
        for col in range(7):
            if row in(0,6) or col in(0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_square():
    """printing  shape of'square' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if i in(0,6) or j in(0,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
