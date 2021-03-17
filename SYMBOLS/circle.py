#Shape of circle:
def for_circle():
    """printing  shape of'circle' using for loop"""
    for row in range(7):
        for col in range(7):
            if row%6==0 and col%6!=0 or col%6==0 and row%6!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_circle():
    """printing  shape of'circle' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if i%6==0 and j%6!=0 or j%6==0 and i%6!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
