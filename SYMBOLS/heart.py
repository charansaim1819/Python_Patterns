#Shape of heart:
def for_heart():
    """printing  shape of'heart' using for loop"""
    for row in range(6):
        for col in range(7):
            if row-col==2 or row+col==8 or col%3!=0 and row==0 or col%3==0 and row==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_heart():
    """printing  shape of'heart' using while loop"""
    i=0
    while i<6:
        j=0
        while j<7:
            if i-j==2 or i+j==8 or j%3!=0 and i==0 or j%3==0 and i==1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
