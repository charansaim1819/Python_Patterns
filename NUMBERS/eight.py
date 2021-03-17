#Shape of num 8:
def for_8():
    """printing number '8' using for loop"""
    for row in range(7):
        for col in range(5):
            if col in(1,2) and row%3==0 or col%3==0 and row%3!=0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()





def while_8():
    """printing number '8' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j in(1,2) and i%3==0 or j%3==0 and i%3!=0 :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

