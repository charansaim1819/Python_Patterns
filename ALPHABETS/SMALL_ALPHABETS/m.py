#Shape of small m:
def for_m():
    """printing small 'm' using for loop"""
    for row in range(5):
        for col in range(8):
            if col%3==1 and row!=0 or row==0 and col in(2,3,5,6) or row==col==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_m():
    """printing small 'm' using while loop"""
    i=0
    while i<5:
        j=0
        while j<8:
            if j%3==1 and i!=0 or i==0 and j in(2,3,5,6) or i==j==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
