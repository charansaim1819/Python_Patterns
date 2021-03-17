#shape of num 2:
def for_2():
    """printing number '2' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==0 and row not in(1,2) or col==1 and row in(0,3,5) or col==2 and row in(1,2,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_2():
    """printing number '2' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==0 and i not in(1,2) or j==1 and i in(0,3,5) or j==2 and i in(1,2,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

