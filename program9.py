#using for loop
color=["Red","Blue","Red"]
for color in color:
    print(color)
    for i in color:
        print(i)


#using range in for loop
for k in range(20):
    print(k+2)

for k in range(5,50,5):
    print(k+5)     


#multiplication table using while loop
x=int(input("Enter the value"))
i=1 #counter 
while i<=10:
    product = x*i
    i = i+1 #increement the counter
    print(product)

#decrementing
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("At the end counter became zero")

    
