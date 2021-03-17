#Shape of small a:
def for_a():
    """printing small 'a' using for loop"""
    for row in range(5):
        for col in range(6):
            if col==0 and row not in(0,4) or col==3 and row not in(0,4) or col in(1,2) and row in(0,4) or col==row==4 or col==5 and row==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_a():
    """printing small 'a' using while loop"""
    i=0
    while i<5:
        j=0
        while j<6:
            if j==3 and i not in(0,4) or i==3 and j not in(1,2,4) or j==0 and i in(1,2) or i==0 and j in(1,2,3) or i==4 and j not in(0,3,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
