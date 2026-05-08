a=int(input("Enter a mark 1:"))
b=int(input("Enter a mark 2:"))
c=int(input("Enter a mark 3:"))
d=int(input("Enter a mark 4:"))
print("Total mark obtained by student:",a+b+c+d)
av=(a+b+c+d)/4
print("Average mark:",(a+b+c+d)/4)
if (av > 75):
    print("Distinction")
elif (60 <= av < 75):
    print("First division")
elif (50 <= av < 60):
    print("Second division")
elif (40 <= av < 50):
    print("Third division")
else:
    print("Fail")
    
        
