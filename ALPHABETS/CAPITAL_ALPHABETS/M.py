#shape of capital M:
def for_M():
    """printing capital 'M' using for loop"""
    for row in range(6):
        for col in range(5):
            if col in(0,4) or row==1 and col!=2 or row ==2 and col==2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_M():
    """printing capital 'M' using while loop"""
    i=0
    while i<6:
        j=0
        while j<5:
            if j in (0,4) or j==1 and i==1 or j==2 and i==2 or j==3 and i==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
