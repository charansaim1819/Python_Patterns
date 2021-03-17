#Shape of small n:
def for_n():
    """printing small 'n' using for loop"""
    for row in range(5):
        for col in range(5):
            if col in(1,4) and row!=0 or row==0 and col not in(1,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_n():
    """printing small 'n' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j in (1,4) and i!=0 or i==0 and j not in (1,4) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
