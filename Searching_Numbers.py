list=[12,123,17352,87654,243,1,5,75,89,342,2345]
a=int(input("Enter a number to be searched"))
i=0
b=0
for i in list:
    if(i==a):
        print("Your number has been found")
        b=1


if(b==0):
    print("Your number hasn't been found")
        


