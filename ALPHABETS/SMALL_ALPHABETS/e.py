#Shape of small e:
def for_e():
    """printing small 'e' using for loop"""
    for row in range(7):
        for col in range(4):
            if col==0 and row not in(0,6) or col in(1,2) and row%3==0 or  col==3 and row in(1,2,5):
                print("*",end=" ")
            else:
                print(" ",end= " ")
        print()




def while_e():
    """printing small 'e' using while loop"""
    i=0
    while i<7:
        j=0
        while j<4:
            if j==0 and i not in(0,6) or i==0 and j in(1,2) or j==3 and i in(1,2,5) or j==1 and i in(0,3,6) or j==2 and i in(0,3,6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

        
