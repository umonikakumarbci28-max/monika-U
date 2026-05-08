for i in range(5):
    for j in range(4):
        if((i in {0,4}) and j in {0,3}):
           print("*",end=" ")
        elif((i in {1,3}) and j in {1,2}):
            print("*",end=" ")
        elif((i==2) and j in {0,1}):
            print("*",end=" ")
        elif((j==0) and i in {0,1,2,3,4}):
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
