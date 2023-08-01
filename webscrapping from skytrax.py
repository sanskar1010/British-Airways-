import pandas as pd
import requests
from bs4 import BeautifulSoup
British_airways=[]
pages=362
for i in range(1,pages+1):
    url=f'https://www.airlinequality.com/airline-reviews/british-airways/page/{i}/'
    html_text=requests.get(url).content
    soup=BeautifulSoup(html_text,'lxml')
    reviews=soup.find_all('div','body')
    for review in reviews:
        d={}
        title=review.find('h2','text_header').get_text()
        name=review.find('span',attrs={'itemprop':'name'}).get_text()
        date=review.find('time',attrs={'itemprop':'datePublished'}).get_text()
        table=review.find('table','review-ratings')
        table_rows=table.find_all('tr')
        for row in table_rows:
            heading=row.find_all('td')[0].get_text()
            value=row.find_all('td')[1]
            if (value.find('span','star fill')!=None):
                d[heading]=len(value.find_all('span','star fill'))
            else:
                d[heading]=value.get_text()
        d['title']=title
        d['name']=name
        d['date']=date
        British_airways.append(d)
my_data=pd.json_normalize(British_airways)
my_data.to_excel(r'C:\Users\DELL\Desktop\sanskar british airways.xlsx')
