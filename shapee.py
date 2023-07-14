import pandas as pd
import time
from seleniumwire import webdriver  # 需安裝：pip install selenium-wire
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
from tqdm import tqdm
from bs4 import BeautifulSoup
from cn2an import cn2an

keyword = '廚具'
page = 1
ecode = 'utf-8-sig'


# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
# 不載入圖片，提升爬蟲速度
# options.add_argument('blink-settings=imagesEnabled=false')

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=options)
time.sleep(random.randint(5, 10))

# 開啟網頁，進到首頁
driver.get('https://shopee.tw/')
time.sleep(random.randint(5, 10))


####################################################################################
###                       至此，請先停下來手動登入帳號，再往後執行                  ###
####################################################################################


# ----------  抓下商品名稱與連結 ----------
print('---------- 開始進行爬蟲 ----------')
tStart = time.time()  # 計時開始
# 準備用來存放資料的陣列
itemid = []
shopid = []
name = []
link = []
price = []
star_rate = []
history_sold = []
shop_location = []

for i in tqdm(range(int(page))):
    driver.get('https://shopee.tw/search?keyword=' +
               keyword + '&page=' + str(i))
    time.sleep(random.randint(5, 10))
    # 滾動頁面
    for scroll in range(6):
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(random.randint(3, 10))

    # 2023/04/20 由於使用selenium取得商品有些不穩定，因此以下換成全部使用bs4去解析
    # 取得商品內容
    for block in driver.find_elements(by=By.XPATH, value='//*[@data-sqe="item"]'):
        # 將整個網站的Html進行解析
        soup = BeautifulSoup(block.get_attribute(
            'innerHTML'), "html.parser").find('a')
        # 商品ID、商家ID、商品連結

        if soup is not None:
            getID = soup.get('href')
            theitemid = int((getID[getID.rfind('.')+1:getID.rfind('?')]))
            theshopid = int(
                getID[getID[:getID.rfind('.')].rfind('.')+1:getID.rfind('.')])
            
            if(theitemid in itemid and theshopid in shopid):  # 重複爬取
                continue

            # 先整理標籤
            get_parent = soup.find(
                'div', {"data-sqe": "name"}).parent.find_all("div", recursive=False)

            # 商品名稱
            if len(get_parent) > 0:  # 確認有資料再進行
                getname = get_parent[0].find('div').text
            else:
                print('抓不到資料，直接是空的')
                continue  # 沒抓到這個商品就別爬了

            # 價格
            if len(get_parent) > 1:  # 確認有資料再進行
                getSpan = get_parent[1].find_all('span')
                counter = []
                for j in getSpan:
                    theprice = j.text
                    theprice = theprice.replace('萬', '')
                    theprice = theprice.replace('$', '')
                    theprice = theprice.replace(',', '')
                    theprice = theprice.replace(' ', '')
                    
                    if theprice != '':
                        counter.append(int(theprice))

                    
            # 星星趴數(/5)        
            if len(get_parent) > 2:
                div_tags = get_parent[2].find_all('div', class_='shopee-rating-stars__lit')
                percentages = [float(div['style'].split(':')[1].strip('%;')) for div in div_tags]
                if(len(percentages)>0):
                    average_percentage = sum(percentages) / len(percentages)
                    get_star_rate = round(average_percentage / 20, 2)
                else:
                    get_star_rate = None

                
            # 出售量    
            if len(get_parent) > 2:
                div_tag = get_parent[2].find_all('div', class_='r6HknA uEPGHT')
                for j in div_tag:
                    get_history_sold = j.text
                    get_history_sold = get_history_sold.replace('已售出', '')
                    get_history_sold = get_history_sold.replace(' ', '')
                    get_history_sold = get_history_sold.replace(',', '')
                    if get_history_sold != None:
                        get_history_sold = cn2an(get_history_sold, "smart")
                    else:
                        get_history_sold = 0
         
                
            # 商家地點    
            if len(get_parent) > 3:
                get_shop_location = get_parent[3].text

                
                
            link.append("https://shopee.tw"+getID)
            itemid.append(theitemid)
            shopid.append(theshopid)
            name.append(getname)
            price.append(sum(counter)/len(counter))
            star_rate.append(get_star_rate)
            history_sold.append(get_history_sold)
            shop_location.append(get_shop_location)

    time.sleep(random.randint(20, 30))  # 休息久一點

# 2023/04/20 先將每頁抓到的商品儲存下來，方便後續追蹤並爬蟲
dic = {
    '商品ID': itemid,
    '賣家ID': shopid,
    '商品名稱': name,
    '商品連結': link,
    '價格': price,
    '星星趴數': star_rate ,
    '歷史銷售量': history_sold,
    '商家地點': shop_location,
    
}
pd.DataFrame(dic).to_csv(keyword + '_商品資料.csv', encoding=ecode, index=False)

tEnd = time.time()  # 計時結束
totalTime = int(tEnd - tStart)
minute = totalTime // 60
second = totalTime % 60
print('資料儲存完成，花費時間（約）： ' + str(minute) + ' 分 ' + str(second) + '秒')




