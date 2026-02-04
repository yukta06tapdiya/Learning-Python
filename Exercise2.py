import time
timestamp=time.strftime('%H:%M:%S')

timestamp=int(time.strftime('%H'))

if(4<=timestamp<12):
    print("its time:",timestamp)
    print("Good Morning")
elif(12<=timestamp<17):
     print("its time:",timestamp)
     print("Good Afternoon")
elif(17<=timestamp<21):
     print("its time:",timestamp)
     print("Good Evening")
else:
     print("its time",timestamp)
     print("Good Night")

