##_______ Public
##_______ Protected
##_______ Private

#___0001 ____Public :
class Company:
    def __init__(self, Company_Name = "Dhilip Pvt.", Monthly_Profit = "50C"):
        self.C_Name = Company_Name
        self.C_Prof = Monthly_Profit
ab = Company()
ac = Company("Move Zhy Pvt.", "200C")

print("Company Name : {} , Company'z Monthly Profit : {}". format(ab.C_Name, ac.C_Prof))
print("Company Name : {} , Company'z Monthly Profit : {}". format(ac.C_Name, ab.C_Prof))

#___0002 ____Protect :
class Detailz_:
    def __init__ (self, Name, Salary):
        self.Name = Name                # Public
        self._Salary = Salary           #Protected
    def user_salary(self):
        print("Salary :" , self._Salary)
x = Detailz_("Dhuruv", "50,000")
print("Name :", x.Name)
x.user_salary()

#___0003 ____Private :
class Data_:
    def __init__ (self, Name, ID, Password):
        self.Name = Name                #Public
        self._ID = ID                   #Protected
        self.__Password =Password       #Private
    def User_ID(self):
        print("User ID :", self._ID)
    def User_Pass(self):
        print("pass :", self.__Password)
yaz = Data_("YazhRoslin", "Yazhrose_23", "Roslin@23")
print("Name :", yaz.Name)
yaz.User_ID()
yaz.User_Pass()

#___0004 _____Getter and Setter :
class Detail_:
    def __init__(self):
        self.__Profit = 120000

    def get_Prof(self):
        return self.__Profit
    
    def set_Prof(self, Prof):
        if Prof > 100000:
            self.__Profit = Prof
        else :
            print("Profit is lessthen 100000 ")

abc = Detail_()
print(abc.get_Prof())
abc.set_Prof(150000)
print(abc.get_Prof())
#abc.set_Prof(9990)



