from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import templates

driver = webdriver.Firefox(executable_path=r'./geckodriver/geckodriver.exe')

houses = {
    "prices":[],
    "addresses":[],
    "dates":[],
    "beds":[],
    "baths":[],
    "cars":[],
    "types":[]
}

for website in templates.websites:
    for x in range(website[2]):
        if x >= website[1]:
            driver.get(website[0].replace("{{number}}", str(x)) + website[3])
            content = driver.page_source
            soup = BeautifulSoup(content)
            print(soup)
            for a in soup.findAll(*website[4]):
                houses["prices"].append(a.find(*website[5]))
                houses["addresses"].append(a.find(*website[6]))
                houses["dates"].append(a.find(website[7]))
                houses["beds"].append(a.find(*website[8]))
                houses["baths"].append(a.find(*website[9]))
                houses["cars"].append(a.find(*website[10]))
                houses["types"].append(a.find(*website[11]))


df = pd.DataFrame({
    'Price':houses["prices"],
    'Address':houses["addresses"],
    'Date Collected':houses["dates"],
    'Bedrooms':houses["beds"],
    'Bathrooms':houses["baths"],
    'Car Spaces':houses["cars"],
    'House Type':houses["types"]
}) 

df.to_csv('houses.csv', index=False, encoding='utf-8')