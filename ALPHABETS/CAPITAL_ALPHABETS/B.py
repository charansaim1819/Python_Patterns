#Shape of capital B:
def for_B():
    """printing capital 'B' using for loop"""
    for row in range(7):
        for col in range(5):
            if col==0 or row==0 and col!=4 or row==3 and col!=4 or row==6 and col!=4 or col==4 and row%3!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
for_B()


def while_B():
    """printing capital 'B' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i==0 and j!=4 or i==3 and j!=4 or i==6 and j!=4 or j==4 and i%3!=0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1
        print()
        i+=1
while_B()
