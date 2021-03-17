#Shape of num 4:
def for_4():
    """printing number '4' using for loop"""
    for row in range(7):
        for col in range(6):
            if col==4 or row==5 or row+col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()







def while_4():
    """printing number '4' using while loop"""
    i=0
    while i<7:
        j=0
        while j<6:
            if j==4 or i==5 or i+j==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

