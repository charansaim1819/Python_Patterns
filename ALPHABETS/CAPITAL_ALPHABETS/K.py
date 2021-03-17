 #Shape of capital K:
def for_K():
     """printing capital 'K' using for loop"""
     for row in range(7):
         for col in range(4):
             if col==0 or row+col==3 or row -col==3:
                 print("*",end=" ")
             else:
                 print(" ",end=" ")
         print()



def while_K():
    """printing capital 'K' using while loop"""
    i=0
    while i<7:
        j=0
        while j<5:
            if j==0 or i+j==3 or i -j==3:
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
