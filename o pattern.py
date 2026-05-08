for i in range(5):
    for j in range(5):
        if((i in {0,4}) and j in {1,2,3}):
            print("*",end=" ")
        elif((i in {1,2,3}) and j in {0,4}):
             print("*",end=" ")
        else:
             print(" ", end=" ")
    print()
