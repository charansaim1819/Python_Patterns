#Shape of num 0:
def for_0():
    """printing number '0' using for loop"""
    for row in range(7):
        for col in range(6):
            if row%6==0 and col%5!=0 or col%5==0 and row%6!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_0():
    """printing number '0' using while loop"""
    i=0
    while i<7:
        j=0
        while j<6:
            if i%6==0 and j%5!=0 or j%5==0 and i%6!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
