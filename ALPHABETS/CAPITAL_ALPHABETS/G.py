#shape of capital G:
def for_G():
    """printing capital 'G' using for loop"""
    for row in range(5):
        for col in range(4):
            if row==2 and col!=1 or row==0 and col  in(1,2,3) or col==0 and row not in(0,4) or row==4 and col in(1,2) or col==3 and row in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_G():
    """printing capital 'G' using while loop"""
    i=0
    while i<5:
        j=0
        while j<4:
            if i==2 and j!=1 or i==0 and j in(1,2,3) or j==0 and i not in(0,4) or i==4 and j in(1,2) or j==3 and i in(2,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
