from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.e-tinex.mk/default.aspx?b=31&p=1&f5=0&&i=96').text 
soup = BeautifulSoup(html_text, 'lxml')

proizvodi = soup.find_all('div', class_ = 'block block_6')


for proizvod in proizvodi:
    proizvod_naziv = proizvod.find('div', class_ = 'desc_grid1').text 
    proizvod_cena = proizvod.find('div', class_ = 'price_cont').text.replace(' ','')
    
    print(f"Производ: {proizvod_naziv.strip()}")
    print(f"Цена: {proizvod_cena.strip()}")
    
    print('')