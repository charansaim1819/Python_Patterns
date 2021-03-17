 #shape of rectangle:
def for_rectangle():
     """printing  shape of'rectangle' using for loop"""
     for row in range(5):
         for col in range(11):
             if row in(0,4) or col in(0,10):
                 print("*",end=" ")
             else:
                 print(" ",end=" ")
         print()




def while_rectangle():
    """printing  shape of'rectangle' using while loop"""
    i=0
    while i<5:
        j=0
        while j<11:
            if i in(0,4) or j in(0,10):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            j+=1  
        print()
        i+=1

    
