class ServiceQuote():
    def __init__(self,pcharge,lcharge,tax,total):
        self.pcharge = pcharge
        self.lcharge = lcharge
        self.tax = .08
        self.total = total

    def setParts(self, pcharge):
        self.pcharge = pcharge

    def setLarbor(self, lcharge):
        self.lcharge = lcharge

    def getParts(self): 
        return self.pcharge

    def getLabor(self):
        return self.lcharge

    def getTax(self):
        return self.tax

    def getTotal(self):
        return (self.pcharge + self.lcharge) * self.tax

estimate1 = ServiceQuote(100,150,.08,)
