#Class and Object
"""
class CName:
    print("Blue girl")
class name:
    y=23
a=name()
print(a)
print(a.y)
"""
"""class Name:
    def __init__ (self, Name, Place):
        self.Name = Name
        self.Place = Place
b=Name("Dhanvi", "Madurai")
print(b.Name)
print(b.Place)

class myself:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def __str__ (self):
        return f'{self.name},{self.age}'
Per=myself("Madhu", 23)
print(Per)

class bluegirl:
    def __init__ (self, funName):
        self.funName = funName
        pass
    def Name(self):
        return f'name: {self.funName}'
new=bluegirl("Dhivya")
print(new.funName)
print(new.Name())
"""


class bio:
    def __init__ (self, Name, DOB, Mobile, Location, Qualification, Mail):
        self.Name = Name
        self.DOB = DOB
        self.Mobile = Mobile
        self.Location = Location
        self.Qualification = Qualification
        self.Mail = Mail
    
    def BioData(self):
        return f'name:{self.Name}, DOB:{self.DOB}, Mobile:{self.Mobile}, Place:{self.Location}, Qualif:{self.Qualification}, Mail_ID:{self.Mail}'
mybio=bio("Name:   Yazh", "DOB:    Nov 5th", "Mobile: 98xxxxxxx3", "Place:  Madurai", "Degree: M.Sc.(Zoology)", "Mail:   as.xxxxx@gamil.com")
print(mybio.Name)
print(mybio.DOB)
print(mybio.Mobile)
print(mybio.Location)
print(mybio.Qualification)
print(mybio.Mail)
"""Name=mybio.Name
DOB=mybio.DOB
Mobile=mybio.Mobile
Place=mybio.Location
Qualif=mybio.Qualification
Mail=mybio.Mail
print("Name:", Name)
print("Date of Birth:", DOB)
print("Mobile:", Mobile)
print("Location:", Place)
print("Qualification:", Qualif)
print("Mail_ID:", Mail)"""
#print(mybio.BioData())


