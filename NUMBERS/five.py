#shape of num 5:
def for_5():
    """printing number '5' using for loop"""
    for row in range(7):
        for col in range(5):
            if row==0 or col==0 and row not in(4,5) or row==3 and col!=4 or col==4 and row not in(1,2,3) or row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()






def while_5():
    """printing number '5' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if i==0 or j==0 and i not in(4,5) or i==3 and j!=4 or j==4 and i not in(1,2,3) or i==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

