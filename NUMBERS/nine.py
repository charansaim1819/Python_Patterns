#Shape of num 9:
def for_9():
    """printing number '9' using for loop"""
    for row in range(8):
        for col in range(5):
            if col in(1,2) and row%3==0 or col==3 and row not in(0,7) or col==0 and row in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_9():
    """printing number '9' using while loop"""
    i=0
    while i<8:
        j=0
        while j<5:
            if j in(1,2) and i%3==0 or j==3 and i not in(0,7) or j==0 and i in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

