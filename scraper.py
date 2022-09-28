from ast import Try
from importlib.resources import contents
# from typing_extensions import Required
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('C:/Users/user/OneDrive/Área de Trabalho/programa/aula127/chromedriver.exe')
browser.get(START_URL)
time.sleep(10)
scarped_data = []
stars_data = []
def scrape():
    
    soup = BeautifulSoup(browser.page_source,'html.parser')

    bright_star_table = soup.find("table", attrs={"class","wikitable sortable jquery-tablesorter"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        # print(table_cols)

        for col_data in table_cols:
            # print(col_data.text)
            data = col_data.text.strip()
            # print(data)

            temp_list.append(data)
            # print(temp_list)
        scarped_data.append(temp_list)
        print(scarped_data)

    for i in range(0,len(scarped_data)):
        Star_name = scarped_data[i][1]
        Distance = scarped_data[i][3]
        Mass = scarped_data[i][5]
        Radius = scarped_data[i][6]
        Lum = scarped_data[i][7]

        Required_data = [Star_name,Distance,Mass,Radius,Lum]
        stars_data.append(Required_data)
scrape()
headers = ['Star_name','Distance','Mass','Radius','Luminosity']
star_df_1 = pd.DataFrame(stars_data, columns = headers)
#exportando em CSV
star_df_1.to_csv('scraped_Data.csv',index = True, index_label ='id')