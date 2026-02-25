s={}
print(type(s))

s=set()
print(type(s))

info={"Carla",5.9,10,"max"}
for value in info:
    print(value)

#Set Methods
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)#s2 will be add in s1
print(s1,s2)

cities={"Mumbai","Pune","Delhi","Kolkatta"}
cities.add("Udaipur")
cities.remove("Mumbai")
cities2={"Nagpur","Chennai","Jaipur","Pune"}
cities3=cities.symmetric_difference(cities2)
print(cities3)
print(cities.issuperset(cities2))
cities.intersection_update(cities2)
print(cities)

#del keyword can delete entire set
#pop can pop up any element from set
#clear help to clear all item in set and print empty set
