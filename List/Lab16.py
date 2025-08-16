# Slicing in List
# -11, -10 -9, -8  -7, -6, -5  -4, -3  -2, -1  --> -Ve Index
#  S    I   M   P   L   I   L   E   A   R   N
#  0,   1,  2,  3,  4,  5,  6,  7,  8,  9, 10  --> +Ve Index

# listObject[X:Y]
# Here ,
# X is start index
# Y is end Index it returns (Y-1)th Value
# also X < Y
myEdtech=['S', 'I', 'M', 'P', 'L', 'I', 'L', 'E', 'A', 'R', 'N']
print(myEdtech[-1:-3]) # [] # -1<-3 = False
print(myEdtech[-10:-3]) # ['I', 'M', 'P', 'L', 'I', 'L', 'E']


