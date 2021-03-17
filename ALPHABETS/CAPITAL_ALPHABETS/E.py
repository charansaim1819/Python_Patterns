#Shape of capital E:
def for_E():
    """printing capital 'E' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 or row in(0,3,6):
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()





def while_E():
    """printing capital 'E' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i%3==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1

