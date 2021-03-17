#Shape of small o:
def for_o():
    """printing small 'o' using for loop"""
    for row in range(5):
        for col in range(5):
            if col%4==0 and row not in(0,4) or row%4==0 and col not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_o():
    """printing small 'o' using while loop"""
    i=0
    while i<5:
        j=0
        while j<5:
            if j%4==0 and i not in(0,4) or i%4==0 and j not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
