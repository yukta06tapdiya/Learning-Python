#custom errors
#in python we can raise custom error by using raise keyword
num=int(input("Enter the integer:"))
if(num<5 or num>10):
    raise ValueError("Integer is not between 5 and 10")

a=input("")
if(a=="quit"):
    print("correct input")
else:
    raise TypeError("input is wrong")