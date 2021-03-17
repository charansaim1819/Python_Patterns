#Shape of num 6:
def for_6():
    """printing number '6' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,6) or col in(1,2) and row%3==0 or col==3 and row in(5,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_6():
    """printing number '6' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 and i not in(0,6) or j in(1,2) and i%3==0 or j==3 and i in(5,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

