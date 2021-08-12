class ATMCard:
    def __init__(self, defaultPin, defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance
    def cekPin(self):
        return self.defaultPin
    def cekSaldo(self):
        return self.defaultBalance