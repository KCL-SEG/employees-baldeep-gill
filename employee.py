"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Pay:
    def __init__(self, type):
        self.type = type

    def get_pay_type(self):
        return self.type

class MonthlyPay(Pay):
    def __init__(self, rate, type="monthly"):
        super().__init__(type)
        self.rate = rate

    def getPayRate(self):
        return self.rate

    def returnPayString(self):
        return f"monthly salary of {self.rate}"

class HourlyPay(Pay):
    def __init__(self, hours, rate, type="hourly"):
        super().__init__(type)
        self.hours = hours
        self.rate = rate

    def getPayRate(self):
        return self.hours * self.rate

    def returnPayString(self):
        return f"contract of {self.hours} hours at {self.rate}/hour"

class Bonus:
    def __init__(self, type):
        self.type = type

    def get_bonus_type(self):
        return self.type

class CommissionBonus(Bonus):
    def __init__(self, contracts, rate, type="commission"):
        super().__init__(type)
        self.contracts = contracts
        self.rate = rate

    def getContractString(self):
        return f"commission for {self.contracts} contract(s) at {self.rate}/contract"

    def getBonusRate(self):
        return self.contracts * self.rate

class BonusBonus(Bonus):
    def __init__(self, rate, type="bonus"):
        super().__init__(type)
        self.rate = rate

    def getContractString(self):
        return f"bonus commission of {self.rate}"

    def getBonusRate(self):
        return self.rate

class Employee(Pay, Bonus):
    def __init__(self, name, payType, bonusType):
        self.name = name
        self.payType = payType
        self.bonusType = bonusType

    def get_pay(self):
        if self.bonusType:
            return self.payType.getPayRate() + self.bonusType.getBonusRate()
        else:
            return self.payType.getPayRate()

    def __str__(self):
        if self.bonusType:
            return f"{self.name} works on a {self.payType.returnPayString()} and receives a {self.bonusType.getContractString()}.  Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} works on a {self.payType.returnPayString()}.  Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyPay(4000), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyPay(100, 25), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyPay(3000), CommissionBonus(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyPay(150, 25), CommissionBonus(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyPay(2000), BonusBonus(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyPay(120, 30), BonusBonus(600))
