#method overriding

"""class shapes:
    def area(self):
        print("this is new shapes")

class circle(shapes):
    def area(self, a):
        print(3.14*a*a)

class square(shapes):
    def area(self,a):
        print(4*a)

circle1=circle()
circle1.area(3)
square1=square()
square1.area(23)"""


"""class Land:
    def Landfeet(self):
        print("40 - 60")
class NewLand(Land):
    def feet(self, a):
        print(11*a)

class OldLand(Land):
    def feet(self, a):
        print(5*a)

New=NewLand()
New.feet(5)
Old = OldLand()
Old.feet(14)"""

"""class RBI:
    def Receive(self):
        print("10%_ of Interest")
class Bank_1(RBI):
    def Receive(self):
        print(self.Receive())
        pass
class Bank_2(RBI):
    def Receive(self, a):
        print("RBI New Interest :", 3.21*a)
class NewBank(RBI):
    def Receive(self, x):
        print("New Bank Interest :", 1.17*x)
B_1 = Bank_1()
#B_1.Receive()
BB = Bank_2()
BB.Receive(2)
B_2 = NewBank()
B_2.Receive(9)"""

"""class Random:
    def Number(self):
        print("values are not eligible")
class Ran(Random):
    def Number(self, ab, xy):
        print(ab*xy+25)
class Ran_1(Random):
    def Number(self, hi, jk):
        print(hi/jk*2)
N_1 = Ran()
N_1.Number(8,5)
N_2 = Ran_1()
N_2.Number(255,5)"""


#method overload

"""class Reading:
    def Book(self):
        print("Reading the Books")
class Reading_2(Reading):
    def Book(self, Name_one, Name_two):
        print(Name_one, Name_two)

class Reading_3(Reading):
    def Book(self, a_Book, b_Book):
        print(a_Book , b_Book)
        print(a_Book + b_Book)
    def Book(self, B_Arts, B_Science, B_Computer):
        print(B_Arts, B_Science, B_Computer)
S = Reading()
#S.Book()
B1=Reading_2()
B1.Book("'Life is Difficult'", "and 'Reading Mind'")
B2=Reading_2()
#B2.Book("'Read the Story'", ", 'Its not wrong'", "and 'Education Methods'")
B3=Reading_3()
B3.Book("'Course Detailz of Arts',", "'Parts of Science'", "and 'Computer Application ==> Information'")"""



