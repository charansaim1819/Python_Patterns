#Shape of small g:
def for_g():
    """printing small 'g' using for loop"""
    for row in range(8):
        for col in range(4):
            if col==3 and row!=1 or row%3==1 and col!=0 or col==0 and row in(2,3,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_g():
    """printing small 'g' using while loop"""
    i=0
    while i<9:
        j=0
        while j<5:
            if j==0 and i in(1,2,4,6,7) or j in(1,2) and i in(0,3,5,8) or j==3 and i in(1,2,6,7) or i==0 and j not in(0,3):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
