from urllib import request, response
import requests
import bs4

url=input("enter the url : ")
response=requests.get(url)
print(response.text)

filename="temp.html"
bs=bs4.BeautifulSoup(response.text,"html.parser")
formatted_text=bs.prettify()
#print(formatted_text)

with open(filename, "w+", encoding="utf-8") as f:
    f.write(formatted_text)
list_img=bs.find_all('img')
# print(list_img)
no_of_images=len(list_img)
list_anc=bs.find_all('a')
no_of_anc=len(list_anc)
print("no.of images",no_of_images)
print("No.of anchors",no_of_anc)



