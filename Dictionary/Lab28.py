# sir if we make changes in duplicate dict will the original dict get changed
employeeDetails={
        1:"Vikash",
        2:"Priyanshu",
        3:"Atul",
        4:"Surya",
        5:"Chiraj",
        6:"Ramesh"
}

print("Original Dictionary :: ",employeeDetails)
duplicate=employeeDetails
print("Copy Dictionary ::",duplicate)
duplicate[1]="Vikash Updated"
print("Original Dictionary :: ",employeeDetails)
print("Updated Dictionary ::",duplicate)
