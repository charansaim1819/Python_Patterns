#Shape of small s:
def for_s():
    """printing small 's' using for loop"""
    for row in range(8):
        for col in range(4):
            if col==0 and row in(1,2,5) or col in(1,2) and row%3==0 or col==3 and row in(1,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_s():
    """printing small 's' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 and i in(1,2,5) or j in(1,2) and i%3==0 or j==3 and i in(1,4,5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
