import sys

class Car:
    pass


# I have created the object of class CAR it will create  the two object
# One object is object1
# Second Object is created in memory by python
object1=Car()
object2=object1
object3=object1
object4=object1
print(sys.getrefcount(object1))
# You can create n number of object for the respective class
