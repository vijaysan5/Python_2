from abc import ABC, abstractmethod

class Mint(ABC):
    def Hello(self):
        pass
class Mind(Mint):
    def Hello(self):
        return "Enjoy your Day"
hi = Mind()
print(hi.Hello())



from abc import ABC, abstractmethod

class Applicant(ABC):
    def __init__ (Self, Name):
        Self.Name = Name
    def Work(self):
        pass
    def Show_Applicant(self):
        print(f'Aplicant Detaiz: {self.Name}')

class Applicant_one(Applicant):
    def Work(self):
        print("Liza pvt. Company Manager")
class  Applicant_two(Applicant):
    def Work(self):
        print("Liza pvt. Company Ass. Manager")

Worker = [Applicant_one("Dhivya"), Applicant_two("Yazhini")]
for w in Worker:
    w.Show_Applicant()
    w.Work()
