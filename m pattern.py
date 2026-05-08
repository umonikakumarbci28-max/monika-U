for i in range(5):
    for j in range(5):
        if((i in{0,3,4}) and j in {0,4}):
            print("M",end=" ")
        elif((i==2) and j in {0,2,4}):
            print("M",end=" ")
        elif((i==1) and j in {0,1,3,4}):
            print("M",end=" ")
        else:
            print(" ",end=" ")
    print()
