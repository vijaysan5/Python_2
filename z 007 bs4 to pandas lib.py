import requests
from bs4 import BeautifulSoup
import pandas as pan

ws = "https://miniaturesshop.com/?srsltid"
req = requests.get(ws)
print(req.status_code)

soup = BeautifulSoup(req.text, "html.parser")

#_________PRODUCT Name :
Product = soup.find_all(class_= "card__heading h5")
# print(Product)

for Pro in Product:
    print(Pro.text)
Product_Name = [Pro.text.strip() for Pro in Product]
print(Product_Name)

#_________PRODUCT PRICE :
Money = soup.find_all(class_="price-item price-item--regular")
print(Money)

Product_Price = {Prc.text.strip() for Prc in Money}

Price=list(Product_Price)
Price.pop(0)
print(Price)
""" a = len(Product_Name)
print(a)
b = len(Product_Price)
print(b) """


Product_Detail = {
    'Name' : Product_Name,
    'Price' : Price
}
Data_Frame = pan.DataFrame(Product_Detail)
print("\n Dataframe : ")
print(Data_Frame)

Data_Frame.to_csv('bs4_file.csv', index=False)
print("Data Saved Successfully...")
read = pan.read_csv('bs4_file.csv')
print("\n CSV _ Reading File : >>>")
print(read)