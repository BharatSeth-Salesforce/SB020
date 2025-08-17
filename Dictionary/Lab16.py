# Dictionary Object are mutable
employeeDetails={
        1:"Vikash",
        2:"Priyanshu",
        3:"Atul",
        4:"Surya",
        5:"Chiraj",
        6:"Ramesh"
       }
print("Before Delete ")
print(employeeDetails)

del employeeDetails[1] # It will delete the one entry
del employeeDetails[2] # It will delete the one entry
del employeeDetails[3] # It will delete the one entry
del employeeDetails[4] # It will delete the one entry
del employeeDetails[5] # It will delete the one entry
del employeeDetails[6] # It will delete the one entry

print("After Delete ")
print(employeeDetails) # {} Empty Dictionary
print(type(employeeDetails)) # {} Empty Dictionary