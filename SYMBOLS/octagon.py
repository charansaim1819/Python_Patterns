#Shape of octagon:
def for_octagon():
    """printing  shape of'octagon' using for loop"""
    for row in range(7):
        for col in range(7):
            if col in(0,6) and row in(2,3,4) or row in(0,6) and col in(2,3,4) or col in(1,5) and row in(1,5)  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
for_octagon()


def while_octagon():
    """printing  shape of'octagon' using while loop"""
    i=0
    while i<7:
        j=0
        while j<7:
            if j in(0,6) and i in(2,3,4) or i in(0,6) and j in(2,3,4) or j in(1,5) and i in(1,5)  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

while_octagon()    
