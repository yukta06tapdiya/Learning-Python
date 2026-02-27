#Exception Handling
a=input("Enter the number:")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)}X {i} ={int(a)*i}")
except:
    print("Sorry some Exception Occurred")

print("Some imp lines of code")
print("End of Program")


try:
    num=int(input("Enter the integer"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Please enter a integer")
except IndexError:
    print("num is not in index")