#Shape of small w:
def for_w():
    """printing small 'w' using for loop"""
    for row in range(5):
        for col in range(7):
            if col%3==0 and row!=4 or col%3!=0 and row==4:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def while_w():
    """printing small 'w' using while loop"""
    i=0
    while i<4:
        j=0
        while j<7:
            if i==0 and j in(0,6) or i in(1,2) and j%3==0 or i==3 and j%3!=0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
