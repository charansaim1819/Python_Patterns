#Shape of small i:
def for_i():
    """printing small 'i' using for loop"""
    for row in range(6):
        for col in range(3):
            if row==5 or col==1 and row!=1 or row==2 and col!=2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()






def while_i():
    """printing small 'i' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==1 and i!=1  or i==2 and j!=2 or i==5 and j!=1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
