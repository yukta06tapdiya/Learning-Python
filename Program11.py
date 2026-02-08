def calculateGmean(a,b):
    
    mean =(a*b)/(a+b)
    print(mean)

def Greaternum(a,b):
    if(a>b):
        print("First is greater")
    else:
        print("Second is greater")
    
def lessernum(a,b):#function declaration
    if(a<b):
        print("First is Lesser")
    else:
        print("Second is Lesser")


a=9
b=8
Greaternum(a,b)#function call
lessernum(a,b)
#gmean1=(a*b)/(a+b)
#print(gmean1)
calculateGmean(a,b)

c=8
d=7
Greaternum(c,d)
lessernum(c,d)
#gmean1=(c*d)/(c+d)
#print(gmean1)
calculateGmean(c,d)


