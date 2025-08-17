# Dictionary Object are mutable
employeeDetails={
        1:"Vikash",
        2:"Priyanshu",
        3:"Atul",
        4:"Surya",
        5:"Chiraj",
        6:"Ramesh"
       }
print("Before clear ")
print(employeeDetails)
del employeeDetails
print("After clear ")
print(employeeDetails) # NameError: name 'employeeDetails' is not defined
#print(type(employeeDetails)) # {} Empty Dictionary