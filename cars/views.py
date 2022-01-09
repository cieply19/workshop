import requests
from bs4 import BeautifulSoup

def get_brands():
    response = requests.get("https://www.autocaros.pl/cars/brands/")
    soup = BeautifulSoup(response.text, 'html.parser')

    soup = soup.findAll('div', attrs={'class':'tecdocBrands__item'})

    brands = {}
    for x in soup:
        y=0
        x=x.find('span')
        brands[y].append(x)
        y +=1
    return brands
