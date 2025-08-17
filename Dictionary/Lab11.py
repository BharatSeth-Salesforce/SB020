employeeDetails={
        1:"Vikash",
        2:"Priyanshu",
        3:"Atul",
        4:"Surya",
        5:"Chiraj",
        6:"Ramesh"
    }
print(employeeDetails[1])
print(employeeDetails[2])
print(employeeDetails[3])
print(employeeDetails[4])
print(employeeDetails[5])
print(employeeDetails[6])
#print(employeeDetails[7]) # KeyError: 7

if  6 in employeeDetails:
        print(employeeDetails[6])
else:
        print("Value is not present for key 6")


if  7 in employeeDetails:
        print(employeeDetails[7])
else:
        print("Value is not present for key 7")
