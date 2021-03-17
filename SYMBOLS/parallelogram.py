#Shape of parallelogram:
def for_parallelogram():
    """printing  shape of'parallelogram' using for loop"""
    for row in range(5):
        for col in range(11):
            if row==0 and col not in(0,1,2,3) or row==4 and col not in(7,8,9,10) or row+col==4 or row+col==10:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_parallelogram():
    """printing  shape of'parallelogram' using while loop"""
    i=0
    while i<5:
        j=0
        while j<11:
            if i==0 and j not in(0,1,2,3) or i==4 and j not in(7,8,9,10) or i+j==4 or i+j==10:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1
n
    
