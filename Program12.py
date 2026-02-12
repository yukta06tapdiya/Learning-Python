#default argumrnts
def average(a,b):
    print("The average is ",(a+b)/2) 
average(4,5)

#default argumrnts
def average(a=9,b=3):
    print("The average is ",(a+b)/2) 
average()
average(5,5)

#keyword arguments:- we can change places
def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
name(mname="Peter",lname="Wesker",fname="John")
