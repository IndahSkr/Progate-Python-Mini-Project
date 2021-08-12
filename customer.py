from atm_card import ATMCard
class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    def checkid(self):
        return self.id
    def checkPin(self):
        return self.custPin
    def checkBalance(self):
        return self.custBalance
    def withdrawBalance(self, nominal):
        self.balance -= nominal
    def depositBalance(self, nominal):
        self.balance += nominal