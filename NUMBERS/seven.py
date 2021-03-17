#Shape of num 7:
def for_7():
    """printing number '7' using for loop"""
    for row in range(6):
        for col in range(6):
            if row==1 or row+col==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()







def while_7():
    """printing number '7' using while loop"""
    i=0
    while i<6:
        j=0
        while j<6:
            if i==1 or i+j==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

