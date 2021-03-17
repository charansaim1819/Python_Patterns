#Shape of capital J:
def for_J():
    """printing capital 'J' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==2 or row==0  or col==1 and row in(5,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_J():
    """printing capital 'J' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if i==0 or j==2 or i==5 and j not in (1,3,4) or i==6 and j  in(1,2)  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
