#  HORROR BOOK NAME >>> Use BeautifulSoup (bs4)
""" import requests
from bs4 import BeautifulSoup

Web_2 = "https://www.bookchor.com/category/200/horror"
rqsts = requests.get(Web_2)

print(rqsts.status_code)

soup = BeautifulSoup(rqsts.text, "html.parser")

Book = soup.find_all(class_= "product-price")
print(Book) 

for Hrb in Book:
    print(Hrb.text)

Horror = [Hrb.text.strip() for Hrb in Book]
print(Horror)"""      # its not work this vscode version


#  PRODUCT NAME >>> Use BeautifulSoup (bs4)
import requests
from bs4 import BeautifulSoup

Web = "https://www.shopfazl.com/collections/bazaar"
rqst = requests.get(Web)

print(rqst.status_code)

soup = BeautifulSoup(rqst.text, "html.parser")

product = soup.find_all(class_= "ProductItem__Title Heading")
# print(product)

for pro in product:
    print(pro.text)

prd = [pro.text.strip() for pro in product]
print(prd)


import requests
from bs4 import BeautifulSoup

Webs = "https://indianartzone.com/style-canvas-paintings-artworks"
Request = requests.get(Webs)

print(Request.status_code)

soup = BeautifulSoup(Request.text, "html.parser")

# Product Name
Product = soup.find_all(class_= "product name product-item-name")
print(Product)

for Pro in Product:
    print(Pro.text)
Product_Name = [Pro.text.strip() for Pro in Product]
print(Product_Name)





