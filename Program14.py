#adding items in tuple
countries=("India","Russia","USA","Ireland")
temp=list(countries)
temp.append("Nepal")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)
print(len(countries))

#or we can create two tuples and add them and form new tuple