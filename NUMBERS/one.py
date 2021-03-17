#Shape of num 1:
def for_1():
    """printing number '1' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==2 or row==6 or row+col==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_1():
    """printing number '1' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==2 or i==6 or i+j==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

