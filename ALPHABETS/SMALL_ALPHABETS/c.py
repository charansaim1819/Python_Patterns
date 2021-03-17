#shape of small c:
def for_c():
    """printing small 'c' using for loop"""
    for row in range(6):
        for col in range(5):
            if col==0 and row not in(0,5) or row in(0,5) and col!=0 or row==1 and col==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_c():
    """printing small 'c' using while loop"""
    i=0
    while i<6:
        j=0
        while j<5:
            if j==0 and i not in(0,5) or i==0 and j not in(0,4) or i==1 and j in(0,4) or i==5 and j not in(0,0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
