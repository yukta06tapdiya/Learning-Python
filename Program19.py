#for loops with else in Python
for i in []:
    print(i)
else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i==4:
        break
   
else:
    print("Sorry no i")#does not execute because loop end at break statement


while i<7:
    print(i)
    i=i+1
    
   
else:
    print("Sorry no i")


for x in range(5):
    print("iteration on {} in for loop".format(x+1))
else:
    print("else block in loop ")
print("Out of the loop")
