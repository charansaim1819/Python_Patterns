#Shape of tiangle pointed down:
def for_triangle_down():
    """printing  shape of'triangle pointed down' using for loop"""
    for row in range(7):
        for col in range(13):
            if row==0 or row==col or row+col==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




def while_triangle_down():
    """printing  shape of'triangle pointed down' using while loop"""
    i=0
    while i<7:
        j=0
        while j<13:
            if i==0 or i==j or i+j==12:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
