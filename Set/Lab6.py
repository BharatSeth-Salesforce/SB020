mySet={11,2,3,4,5,6,7}

i=0
while(i<len(mySet)):
    print(mySet[i]) # TypeError: 'set' object is not subscriptable
    i=i+1