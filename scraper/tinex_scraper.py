from bs4 import BeautifulSoup
import requests





for x in range(1,13):
    
    url = ('https://www.e-tinex.mk/default.aspx?b=31&p=0')
   
    html_text = requests.get(url+str(x)).text
    soup = BeautifulSoup(html_text, 'lxml')
    
    proizvodi = soup.find_all('div', class_ = 'block block_6')
    
    for proizvod in proizvodi:
        proizvod_naziv = proizvod.find('div', class_ = 'desc_grid1').text 
        proizvod_cena = proizvod.find('div', class_ = 'price_cont').text.replace('\r\n', '').replace('\xa0', '').replace(' ', '')
        
        
        print(f"Производ: {proizvod_naziv.strip()}")    
        print(f"Цена: {proizvod_cena.strip()}")    
           
        

        
