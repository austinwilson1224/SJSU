import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime as dt

baseball = pd.read_csv('Baseball_original.csv')
basketball = pd.read_csv('Basketball_original.csv')
football = pd.read_csv('Football_original.csv')
non_sport = pd.read_csv('NonSport_original.csv')

# create selenium web driver
op = webdriver.ChromeOptions()

# comment the below line out if you want to see the web browser
# op.add_argument('headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options = op)

dnp_bball_url = baseball['D&P Cards url'][2]
print(dnp_bball_url)

#[DNP example](https://dandpsportscards.com/collections/new-releases/products/2020-topps-update-series-baseball-hobby-box-presale)
![alt text](DNP-bball.png "Title")
![alt text](DNP-bball-CSS-class.png "Title")


# UDF for fetching prices for D&P cards 
def get_price_dnp(url, driver = driver):
    try:
        driver.get(url)

    except:
        print('URL not found')
        return 'N/A'

    try:
        price_box = driver.find_element_by_class_name("product-single__price")
        print(price_box)
        print(type(price_box))
        

        price_box = price_box.text
        print(price_box)

        price_box = price_box.strip("$")
        print(price_box)
        return float(price_box)# .strip("$")
    except:
        print("price box dne")
        return '/404/' 


dnp_bball_price_example = get_price_dnp(url = dnp_bball_url)
p2 = get_price_dnp(url = dnp_bball_url)

blowout_bball_url = baseball['Blow out url'][2]
print(blowout_bball_url)

[Blowout example](https://www.blowoutcards.com/2020-topps-update-series-baseball-hobby-box.html)

![alt text](Blowout_baseball.png "Title")


# blowout cards scrapper 
def get_price_blowout(url, driver = driver, class_name = "price-box"):
    try:
        driver.get(url)
    except:
        print('URL not found')
        return 'N/A'
        
    try:
        price_box = driver.find_element_by_class_name("price-box").text
        prices = price_box.split("\n")
        print(prices)
        # case where there is a sale and the original price is listed with the updated price
        # select the second price 
        if len(prices) > 1:
            index = prices[1].index("$")
            print(prices[1][index:].strip("$"))
            return float(prices[1][index:].strip("$"))
        print(prices[0].strip("$"))
        return float(prices[0].strip("$"))
    except:
        print('URL not found')
        return 'N/A'



blowout_baseball_example = get_price_blowout(blowout_bball_url)
p5 = get_price_blowout(blowout_bball_url)
p5


steel_city_url = baseball['Steel City url'][2]
print(steel_city_url)


![alt text](steel_city_baseball.png "Title")


# get prices steel city
def get_price_steel_city(url, driver = driver):
    if url == 'N/A':
        print('no url in file')
        return 'N/A'
    try:
        driver.get(url)
    except:
        print('URL not found')
        return 'N/A'

    try:
        price_box = driver.find_element_by_class_name("p-price").text
        prices = price_box.split(" ")
        print(prices)
        return float(prices[0].strip("$"))
    except:
        print("price box dne")
        return 'N/A'


p3 = get_price_steel_city(steel_city_url)

dave_adams_url = baseball['Dave & Adams url'][2]
print(dave_adams_url)

[Dave & Adams example](https://www.dacardworld.com/sports-cards/2020-topps-update-series-baseball-hobby-box)

def get_price_dave_adams(url, driver = driver):
    try:
        driver.get(url)
    except:
        print('URL not found')
        return 'N/A'

    try:
        price_box = driver.find_element_by_class_name("pricing").text
        prices = price_box.split("\n")
        print(prices)
        if len(prices) > 1:

            print(prices[1].strip("$"))
            return float(prices[1].strip("$"))
        else:
            print(prices[0].strip("$"))
            return float(prices[0].strip("$"))
    except:
        print('price box dne')
        return 'N/A'


p1 = get_price_dave_adams(dave_adams_url)

# UPDATED FUNCTION
def get_price_dave_adams2(url, driver = driver):
    try:
        driver.get(url)
    except:
        print('URL not found')
        return 'N/A'

    try:
        price_box = driver.find_element_by_class_name("price").text #not "price large"
        print(price_box)
        prices = price_box.split("\n")
        print(prices)
        if len(prices) > 1:

            print(prices[1].strip("$"))
            return float(prices[1].strip("$"))
        else:
            print(prices[0].strip("$"))
            return float(prices[0].strip("$"))
    except:
        print('price box dne')
        return 'N/A'


p1 = get_price_dave_adams2(dave_adams_url)

rbicru_url= baseball['RbiCru7 url'][2]
print(rbicru_url)


[RbiCru7 example](https://rbicru7.com/products/2020-topps-update-series-hobby-baseball-box?_pos=1&_sid=8819265bf&_ss=r)


def get_price_rbicru7(url, driver = driver):
    try:
        driver.get(url)

    except:
        print('URL not found')
        return 'N/A'

    try:
        price_box = driver.find_element_by_class_name("product-single__price").text
        return float(price_box.strip("$"))
    except:
        print("price box dne")
        return '/404/'

p4 = get_price_rbicru7(rbicru_url)
p4

date = str(dt.today().strftime('%Y %m %d'))
date


new_row = {"date": date, "product_id": 1, "p1":p1, "p2":p2, "p3":p3, "p4":p4, "p5":p5}

import sqlite3
conn = sqlite3.connect('test1.db')
cur = conn.cursor()

product_id = 1
cur.execute(f'insert into prices values ({date}, {product_id}, {p1}, {p2}, {p3}, {p4}, {p5})')

conn.commit()
conn.close()

def extract_url_data():
    pass
def row_builder(date, product_id, p1, p2, p3, p4, p5):
    return {"date": date, "product_id": product_id, "p1": p1, "p2": p2, "p3": p3, "p4": p4, "p5": p5}

def row_builder_by_url(da_url, dp_url, sc_url, rc_url, b_url):
    return {

        
        "p1" : get_price_dave_adams2(da_url),
        "p2" : get_price_dnp(dp_url),
        "p3" : get_price_steel_city(sc_url),
        "p4" : get_price_rbicru7(rc_url),
        "p5" : get_price_blowout(b_url)
    }

def get_prices(da_url, dp_url, sc_url, rc_url, b_url):
    return get_price_dave_adams2(da_url), get_price_dnp(dp_url), get_price_steel_city(sc_url), get_price_rbicru7(rc_url), get_price_blowout(b_url)

date = str(dt.today().strftime('%Y%m%d'))
product_id = 1
p1 = get_price_dave_adams2(dave_adams_url)
p2 = get_price_dnp(url = dnp_bball_url)
p3 = get_price_steel_city(steel_city_url)
p4 = get_price_rbicru7(rbicru_url)
p5 = get_price_blowout(blowout_bball_url)
# new_row = row_builder(date = date, product_id = product_id, p1 = p1, p2 = p2, p3 = p3, p4 = p4, p5 = p5)


def write_row(row):
    conn = sqlite3.connect('test1.db')
    cur = conn.cursor()
    cur.execute(f'insert into prices values ({row["date"]}, {row["product_id"]}, {row["p1"]}, {row["p2"]}, {row["p3"]}, {row["p4"]}, {row["p5"]})')
    conn.commit()
    conn.close()

write_row(new_row)

# pipeline reading in new format for business stakeholders
baseball_products = pd.read_excel("data/baseball_products.xlsx")
baseball_prices = pd.read_excel("data/baseball_prices.xlsx")

baseball_products.head()
baseball_prices.head()

def get_all_prices_all_products(products): 
    # date
    date = str(dt.today().strftime('%Y%m%d'))
    product_id = products['product_id']

    conn = sqlite3.connect('test1.db')
    cur = conn.cursor()
    #cur.execute(f'')
    # result = pd.DataFrame(columns=['Product Name', 'D&P Price', 'Blowout Price', 'Steel City Price',
    #    'D&A Price','RbiCru7 Price','D&P Cards url','Blow out url','Steel City url',
    #    'Dave & Adams url','RbiCru7 url'])
    # iterate through each row
    for row in products.iterrows():
        index, row = row[0], row[1]
        #row = row[1]
        print(index)
        # D&P cards url
        dp_url = row['D&P Cards url']
        dp_price = get_price_dnp(dp_url)
        # blowout
        blowout_url = row['Blow out url']
        blowout_price = get_price_blowout(blowout_url)
        # steel city
        steel_city_url = row['Steel City url']
        steel_city_price = get_price_steel_city(steel_city_url)
        # dave adams 
        dave_adams_url = row['Dave & Adams url']
        dave_adams_price = get_price_dave_adams2(dave_adams_url)
        # rbicru 
        rbicru7_url = row['RbiCru7 url']
        rbicru7_price = get_price_rbicru7(rbicru7_url)

        row_to_write = {
            "date": date,
            "product_id": product_id,
            "p1": dave_adams_price, 
            "p2": dp_price, 
            "p3": steel_city_price, 
            "p4": rbicru7_price, 
            "p5": blowout_price
        }

        # database



        date = str(dt.today().strftime('%Y%m%d'))
        product_id = row['product_id']
        write_row(row_to_write)
        # p1 = get_price_dave_adams2(dave_adams_url)
        # p2 = get_price_dnp(url = dnp_bball_url)
        # p3 = get_price_steel_city(steel_city_url)
        # p4 = get_price_rbicru7(rbicru_url)
        # p5 = get_price_blowout(blowout_bball_url)
        # new_row = row_builder(date = date, product_id = product_id, p1 = p1, p2 = p2, p3 = p3, p4 = p4, p5 = p5)

        # cur.execute(f'insert into prices values ({date}, {product_id}, {dave_adams_price}, {dp_price}, {steel_city_price}, {rbicru7_price}, {blowout_price})')
        # conn.commit()
        # conn.close()
        # new_row = {
        #     'Product Name': row['Product Name'],
        #     'D&P Price': dp_price, # row['D&P Price '], 
        #     'Blowout Price': blowout_price, # row['Blowout Price'], 
        #     'Steel City Price': steel_city_price, # row['Steel City Price'],
        #     'D&A Price': dave_adams_price, #  row['D&A Price'], 
        #     'RbiCru7 Price': rbicru7_price,
        #     'D&P Cards url': row['D&P Cards url'], 
        #     'Blow out url': row['Blow out url'], 
        #     'Steel City url': row['Steel City url'],
        #     'Dave & Adams url': row['Dave & Adams url'],
        #     'RbiCru7 url': row['RbiCru7 url']}
        #result.append(new_row, )
        # result.loc[index] = new_row
    # return result

get_all_prices_all_products(baseball_products)