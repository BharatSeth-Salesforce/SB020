employeeDetails={
        1:"Vikash",
        2:"Priyanshu",
        3:"Atul",
        4:"Surya",
        5:"Chiraj",
        6:"Ramesh",
        600:"Viraj"
       }

print(employeeDetails)
employeeDetails.setdefault(600,"I am default Value")
print(employeeDetails[600]) 
print(employeeDetails)

