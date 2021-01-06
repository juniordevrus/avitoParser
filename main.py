import requests
from bs4 import BeautifulSoup as bs
import os
import json

urlTrue = "https://www.avito.ru"
numberPage = "?cd=1&p="
countPage = 1
global cardTamplate
cycle = 0
cardTamplate = {}
def parse(source, cycle):
    count = cycle * 50
    soup = bs(source, "html.parser")
    card = soup.findAll("div", class_="iva-item-body-NPl6W")
    for item in card:
        global cardTamplate
        cardTamplate = {
        'id':count,
        'title':'',
        'price':'',
        'link':''
    }

        try:
            name = item.find("span", class_="title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc text-text-1PdBw text-size-s-1PUdo text-bold-3R9dt").get_text()
            cardTamplate["title"] = name
        except:
            continue
        try:
            price = item.find("span", class_="price-text-1HrJ_ text-text-1PdBw text-size-s-1PUdo").get_text()
            cardTamplate["price"] = price
        except:
            continue
        try:
            link = item.find("a", class_="link-link-39EVK link-design-default-2sPEv title-root-395AQ iva-item-title-1Rmmj title-list-1IIB_ title-root_maxHeight-3obWc").get("href")
            cardTamplate["link"] = "https://www.avito.ru" + link
        except:
            continue
        try:
            with open("response.json", "a+", encoding="utf-8") as file:
                json.dump(cardTamplate, file, indent=8,ensure_ascii=False)
                count += 1
        except:
            continue

while True:
    print("Parser Avito")
    URL = input("Write here your url: ")

    if not URL.startswith("https://www.avito.ru/"):
        print("Неверный формат url. 'https://www.avito.ru/'")
        input()
        os.system("cls")
    else:
        os.system("cls")
        break

while True:

    URL = URL + numberPage + str(countPage)
    response = requests.get(URL)
    parse(response.text,cycle)
    countPage = countPage + 1
    cycle = cycle + 1
