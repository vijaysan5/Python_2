"""Oops ==> Object Oriented
Programming in python"""




# 0001. Single Inheritance :
## No.01
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')
ab=Blue("Krishnan", "Yazh")
ab.san()

class Girl(Blue):
    pass

ac=Girl("Vishnu", "Dhiya")
ac.san()"""
## No.02
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')

class Girl(Blue):
    def __init__(self, NameOne, NameTwo):
        Blue.__init__(self, NameOne, NameTwo)

xy=Blue("Krishnan", "Yazh")
xy.san()"""
## No.03
"""class Blue:
    def __init__ (self, NameOne, NameTwo):
        self.NameOne = NameOne
        self.NameTwo = NameTwo

    def san (self):
        print(f'{self.NameOne}, {self.NameTwo}')

class Girl(Blue):
    def __init__(self, NameOne, NameTwo):
        super().__init__(self, NameOne, NameTwo)

abc=Blue("Krishnan", "Yazh")
abc.san()"""


# 0002. Multiple Inheritance :
"""class Add:
    def __init__(self, ab, xy):
        self.a = ab
        self.x = xy
    def Adding(self):
        return self.a + self.x

class Multiple:
    def __init__(self, ab, xy):
        self.a = ab
        self.x = xy
    def Multix(self):
        return self.a * self.x

class Add_and_Multiple(Add, Multiple):
    def __init__(self, ab, xy):
        self.a =ab
        self.x = xy
    def  Class_Add_Multi(self):
        Addition = Add.Adding(self)
        Multiplication = Multiple.Multix(self)
        return (Addition, Multiplication)
    
ABC = Add_and_Multiple(3,5)
print("Add:", ABC.Adding())
print("Multiplication:", ABC.Multix())
print("Add & Multix:", ABC.Class_Add_Multi())"""

    
# 0003. Multi level Inheritance :
"""class User_One:
    def User_One(self):
        print("Good Morning to All...!")
class User_Two(User_One):
    def User_Two(self):
        print("Have a Beautiful Day *_*")
class User_Three(User_Two):
    def User_Three(self):
        print("How is going Today?")

Users = User_Three()

Users.User_One()
Users.User_Two()
Users.User_Three()"""


# 0004. Hierarchical Inheritance :
"""class san_v:
    def san_v(self):
        print("Welcome")
class san_one(san_v):
    def san_one(self):
        print("Student number One_1")
class san_two(san_v):
    def san_two(self):
        print("Student number two_2")
Name_1 = san_one()
Name_2 = san_two()

Name_1.san_v()
Name_1.san_one()
Name_2.san_v()
Name_2.san_two()
"""


# 0005. Hybrid Inheritance :
##___01 :
"""class Blue:
    def __init__ (self, RollNumber):
        self.RollNumber = RollNumber
    def san (self):
        print(f'{self.RollNumber}')

class Girl(Blue):
    def girl(self):
        print(f'{self.RollNumber}')
    
class PlayWell:
    def __init__(self, Word):
        self.Word = Word
    def Play(self):
        print("Well Played")

class NewPlay(Girl, PlayWell):
    def new(self):
        self.girl()
        self.Play()

Name_1 = NewPlay("4385")
Name_1.new()"""
##___02 :
"""class FileHandle:
    def Name(self):
        print("Name is Selected")

class sana:
    def __init__ (self, Mean):
        self.Mean = Mean
    def yazh(self):
        print(f'{self.Mean}')
class visible(sana):
    def __init__(self, Mean):
        super().__init__(Mean)
    def seen(self):
        print(f'{self.Mean}')

class Wellwiz(FileHandle, visible):
    def livein(self):
        self.Name()
        self.seen()
Username = Wellwiz("Happy Forever")
Username.livein()"""

##______Ex_:
"""class Employ_Data:
    def __init__(self, Name, ID_number, Position, Company):
        self.N = Name
        self.ID = ID_number
        self.Pos = Position
        self.Com = Company
    def detaiz(self):
        print(f'Name: {self.N}, ID.Number: {self.ID}, Post: {self.Pos}, Company: {self.Com}')

class Employ_College:
    def __init__(self, Persentage, College_name):
        self.Per = Persentage
        self.CN = College_name
    def cg_detailz(self):
        print(f'Persentage: {self.Per}, College Name: {self.CN}')
class Employ_School:
    def __init__(self, SSLC_Mark, SSLC_School, HSC_Mark, HSC_School):
        self.sslc = SSLC_Mark
        self.sslcs = SSLC_School
        self.hsc = HSC_Mark
        self.hscs = HSC_School
    def School_detailz(self):
        print(f'SSLC: {self.sslc}, School: {self.sslcs}')
        print(f'HSC School Data     ==> HSC: {self.hsc}, School: {self.hscs}')

class Employ_Detailz(Employ_Data, Employ_College, Employ_School):
    def Full(self):
        Data = Employ_Data.detaiz(self)
        College = Employ_College.cg_detailz(self)
        School = Employ_School.School_detailz(self)
        return (Data, College, School)
Dtz = Employ_Detailz("Francis", "5A0814", "Ass. Manager", "DOS.Pv.ltd")
Dtz_c = Employ_College("85%", "Aadhi's Arts and Science College")
Dtz_s = Employ_School("409", "DD Hr. Sec. School", "578", "Sara Metric. Hr. Sec. School")
print("Employ Company Data", end=" ==> ")
print(Dtz.detaiz())
print("College Data", end="        ==> ")
print(Dtz_c.cg_detailz())
print("SSLC School Data", end="    ==> ")
print(Dtz_s.School_detailz())"""


