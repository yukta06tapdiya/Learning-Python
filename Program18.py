dic={344:"Harry"
     ,56:"Shubham",
     221:"Neha",
     567:"Arpan"}
print(dic[567])

#dictionary Methods
ep1={122:46,567:89,324:72,522:66}
ep2={222:64,438:91}
ep1.update(ep2)#add ep2 in ep1
ep1.pop(324)#remove key element
ep1.popitem()#removes last element
print(ep1)
