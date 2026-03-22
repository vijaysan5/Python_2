#Create a new Folder :
"""Sanfolder= open("VS_Base.text",'x')
print("File is Created")"""
'''
abc=open("VS_Base.text", 'a')
abc.write("\nGood Morning!")

with open("VS_Base.text", 'w') as like:
    like.write("\nHave a nice day to all...!")

users=open("VS_Base.text", 'a')
users.write("\nHappy Birthday Dear Friend!")
print("Created")

with open("VS_Base.text", 'r') as file:
    look = file.readline()
    print(look)
    print(file.readline())
'''
# Create San.Bio Folder
"""San_1=open("San.Bio", 'x')
print("Bio Page is created")
"""
# San BIO DATA
"""with open("San.Bio",'w') as bio:
    bio.write("BIO DATA")
    bio.write("\n Name   : SANGAVI A")
    bio.write("\n Mobile : 86xxxxxx27")
    bio.write("\n Degree : M.A., D.SS.,")
    bio.write("\n Mail ID: am.xxx@gmail.com")
    print("San Bio is Created")
"""
# Detailz 
"""Detailz=open ("San.Bio", 'w')
Detailz.write("  NAME       PHONE     QUALIFICATION  JOINING")
Detailz.write("\nSandhiya   91xxxxxx98    M.Sc.,       03/2021")
Detailz.write("\nDhanvi     98xxxxxx09    M.Com.,      12/2023")
Detailz.write("\nHarini     74xxxxxx87    HSC          12/2022")
Detailz.write("\nJenifer    93xxxxxx23    MBA          05/2025")
"""
#Delete Option
"""import os
os.remove("VS_Base copy.text")"""

#Error > try\except\finally
"""try:
    san = open("D:\Sangavi A\San Fold - Python\python new as\File Handling_san\VS_Base.text")
    ABC = san.read()
    print(ABC)
    print("folder is open")
except:
    print("folder is not such")
finally:
    print("Completed")"""

# encode() to decode()
"""x=("Happy Birthday")         # decode
abc=x.encode()
print(abc)                      # encode
y=abc.decode()
print(y)                    # decode
"""

