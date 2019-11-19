class Customer():
    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address = address

    def setPhone(self,phone):
        self.phone = phone

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

customer1 = Customer('Kell','3808 Y street', '3605536809')
print(customer1.getPhone(),customer1.getAddress(),customer1.getPhone())