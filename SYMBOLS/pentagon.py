#Shape of pentagon:
def for_pentagon():
    """printing  shape of'pentagon' using for loop"""
    for row in range(7):
        for col in range(9):
            if row+col==4 or row-col==-4 or row==6 and col not in(0,1,7,8)  or row-col==4  or row+col==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_pentagon():
    """printing  shape of'pentagon' using while loop"""
    i=0
    while i<7:
        j=0
        while j<9:
            if i+j==4 or i-j==-4 or i==6 and j not in(0,1,7,8)  or i-j==4  or i+j==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
