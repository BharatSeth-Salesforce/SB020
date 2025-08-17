class Mycompany:
    def __init__(self,companyName,companyAddress,companyType):
        self.companyName=companyName
        self.companyAddress = companyAddress
        self.companyType=companyType

    def getCompanyinfo(self):
        print("Company Name :", self.companyName)
        print("Company Address :", self.companyAddress)
        print("Company Type :", self.companyType)

