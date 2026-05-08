for i in range(5):
    for j in range(5):
        if((i in {0,4}) and j in {0,4}):
            print("*",end=" ")
        elif((i==1) and j in {0,1,4}):
            print("*",end=" ")
        elif((i==2) and j in {0,2,4}):
            print("*",end=" ")
        elif((i==3) and j in {0,3,4}):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
