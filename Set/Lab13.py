mySet1={1,2,3,4,5,6,7,8,100}
mySet2={1,2,3,4,5,6,7,8,9,10,11,12}
newSet=mySet1.difference(mySet2) # All element are in mySet1 but not in mySet2
print(newSet) #{100}

newSet1=mySet2.difference(mySet1) # All element are in mySet2 but not in mySet1
print(newSet1) # {9, 10, 11, 12}