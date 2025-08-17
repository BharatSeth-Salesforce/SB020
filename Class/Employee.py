class Employee:
    _employeeName="Bassy"
    _employeeAge=34
    _employeeSalery=1400
    _employeeId="A101"

    def __init__(self):
        print("--I am default Constructor--")
        self.employeeName="Khalinder"
        self.employeeAge=22
        self.employeeSalery=3000
        self.employeeId="KH-001"

    def getEmployeeDetails(self):
        print("--I am getEmployeeDetails--")
        print("--Employee Name :: ", self._employeeName)
        print("--Employee Age :: ", self._employeeAge)
        print("--Employee Salary :: ", self._employeeSalery)
        print("--Employee ID :: ", self._employeeId)