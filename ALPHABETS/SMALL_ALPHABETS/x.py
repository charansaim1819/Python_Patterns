#Shape of small x:
def for_x():
    """printing small 'x' using for loop"""
    for row in range(5):
        for col in range(5):
            if row%4==0 and col!=2 or col==2 and row not in(0,4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_x():
    """printing small 'x' using while loop"""
    i=0
    while i<4:
        j=0
        while j<5:
            if j!=2 and i%3==0 or j==2 and i in(1,2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
