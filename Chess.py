
row=int(input("Please Enter a number for row :"))
col=int(input("Please Enter a number for col :"))

for i in range(row):
    for j in range(col):
        if (i+j) %2==0:            
             print("#" , end=" ")
        else:
             print("*" , end=" ")
    print()
