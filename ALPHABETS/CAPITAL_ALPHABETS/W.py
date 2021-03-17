#Shape of capital W:
def for_W():
    """printing capital 'W' using for loop"""
    for row in range(4):
        for col in range(13):
            if row-col==0 or row+col==6 or col-row==6 or row+col==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_W():
    """printing capital 'W' using while loop"""
    i=0
    while i<4:
        j=0
        while j<13:
            if i-j==0 or i+j==6 or j-i==6 or i+j==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
