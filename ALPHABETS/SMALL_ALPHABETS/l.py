#Shape of small l:
def for_l():
    """printing small 'l' using for loop"""
    for row in range(6):
        for col in range(3):
            if col==1 or row==0 and col!=2 or row==5 and col!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_l():
    """printing small 'l' using while loop"""
    i=0
    while i<6:
        j=0
        while j<3:
            if j==1 or i==0 and j!=2 or i==5 and j!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
