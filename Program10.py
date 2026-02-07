#using continue statement
for i in range(20):
    if(i==10):
     print("Skip the iteration")
     continue
    print("5X",i,"=",5*i)

#using break statement
for i in range(20):
    if(i==10):
     break
    print("5X",i,"=",5*i)


for i in range(1,100,1):
   print(i,end=" ")
   if(i==50):
      break
   else:
      print("Mississippi")
print("Thank You")