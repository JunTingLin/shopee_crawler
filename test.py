# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 20:25:42 2023

@author: junting
"""

from bs4 import BeautifulSoup

# 準備用來存放資料的陣列
itemid = []
shopid = []
name = []
link = []
price = []
star_rate = []
history_sold = []
shop_location = []


htmlText = '<div class="col-xs-2-4 shopee-search-item-result__item" data-sqe="item"><a data-sqe="link" href="/【免運】簡易櫥櫃-不鏽鋼洗手盆-經濟型櫃子廚房一體灶台櫃-置爐台-三件式流理台-不鏽鋼廚房設備單洗槽.流理台-i.907959200.22636294381?sp_atk=f57cfab0-987c-4320-9251-6c8553b030b8&amp;xptdk=f57cfab0-987c-4320-9251-6c8553b030b8"><div class="tWpFe2"><div class="VTjd7p whIxGK"><div style="pointer-events: none;"><div class="yvbeD6 KUUypF"><img width="invalid-value" height="invalid-value" alt="【免運】簡易櫥櫃 不鏽鋼洗手盆 經濟型櫃子廚房一體灶台櫃 置爐台 三件式流理台  不鏽鋼廚房設備單洗槽.流理台" class="_7DTxhh vc8g9F" style="object-fit: contain" src="https://down-tw.img.susercontent.com/file/tw-11134201-7qukw-lf2f346f2f5b0b_tn"><div class="GOgNtl"><div class="NTmuqd _3NQO+7 WVxeBE _4ycSOm"><span aria-label="promotion"></span><span class="percent">9.5</span><span class="Th6IF+ +b7jwE">折</span></div></div><div class="F7xq8U"><div aria-hidden="true"><div aria-hidden="true" class="Sh+UIZ" data-sqe="ad">Ad</div> </div></div><div class="IpGwg7"><div class="customized-overlay-image"><img alt="overlay image" src="https://down-tw.img.susercontent.com/file/tw-50009109-1d605d93931239411bd41d5d64755e33" width="" height=""></div></div></div></div><div class="KMyn8J"><div class="dpiR4u" data-sqe="name"><div class="FDn--+"><div aria-hidden="true" class="ie3A+n bM+7UW Cve6sh">【免運】簡易櫥櫃 不鏽鋼洗手盆 經濟型櫃子廚房一體灶台櫃 置爐台 三件式流理台  不鏽鋼廚房設備單洗槽.流理台</div></div><div class="FD2XVZ"><div aria-hidden="true" style="display: flex;"><div class="_1PWkR nt-medium nt-foot _3nkRL" style="color: rgb(246, 145, 19);"><svg class="_2DRZW _2xFcL" viewBox="-0.5 -0.5 4 16"><path d="M4 0h-3q-1 0 -1 1a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3q0 1 1 1h3" stroke-width="1" transform="" stroke="currentColor" fill="#f69113"></path></svg><div class="_1FKkT _3Ao0A" style="color: white; background-color: rgb(246, 145, 19);">滿額折$50</div><svg class="_2DRZW _2xFcL" viewBox="-0.5 -0.5 4 16"><path d="M4 0h-3q-1 0 -1 1a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3v0.333a1.2 1.5 0 0 1 0 3q0 1 1 1h3" stroke-width="1" transform="rotate(180) translate(-3 -15)" stroke="currentColor" fill="#f69113"></path></svg></div></div><div aria-hidden="true" class="djt+SZ">滿額贈</div></div></div><div class="hpDKMN"><div class="vioxXd rVLWG6"><span aria-label="current price"></span><span class="recFju">$</span><span class="ZEgDH9">1,606</span> - <span aria-label="current price"></span><span class="recFju">$</span><span class="ZEgDH9">8,007</span></div></div><div class="ZnrnMl"><div class="RS7p+X" data-sqe="rating"><div class="shopee-rating-stars"><div class="shopee-rating-stars__stars"><div class="shopee-rating-stars__star-wrapper"><div class="shopee-rating-stars__lit" style="width: 100%;"><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__gold-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__dark-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><div class="shopee-rating-stars__star-wrapper"><div class="shopee-rating-stars__lit" style="width: 100%;"><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__gold-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__dark-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><div class="shopee-rating-stars__star-wrapper"><div class="shopee-rating-stars__lit" style="width: 100%;"><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__gold-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__dark-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><div class="shopee-rating-stars__star-wrapper"><div class="shopee-rating-stars__lit" style="width: 100%;"><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__gold-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__dark-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><div class="shopee-rating-stars__star-wrapper"><div class="shopee-rating-stars__lit" style="width: 35.7143%;"><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__gold-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div><svg enable-background="new 0 0 15 15" viewBox="0 0 15 15" x="0" y="0" class="shopee-svg-icon shopee-rating-stars__dark-star icon-rating-solid"><polygon points="7.5 .8 9.7 5.4 14.5 5.9 10.7 9.1 11.8 14.2 7.5 11.6 3.2 14.2 4.3 9.1 .5 5.9 5.3 5.4" stroke-linecap="round" stroke-linejoin="round" stroke-miterlimit="10"></polygon></svg></div></div></div></div><div class="r6HknA uEPGHT">已售出 36</div></div><div class="zGGwiV"><span aria-label="from"></span>臺北市中正區</div></div><div class="shopee-item-card__hover-footer _6o9eaa">找相似</div></div></div></a></div>'

soup = BeautifulSoup(htmlText, "html.parser").find('a')

getID = soup.get('href')
theitemid = int((getID[getID.rfind('.')+1:getID.rfind('?')]))
theshopid = int(
    getID[getID[:getID.rfind('.')].rfind('.')+1:getID.rfind('.')])
     
# 先整理標籤
get_parent = soup.find(
    'div', {"data-sqe": "name"}).parent.find_all("div", recursive=False)



# 商品名稱
if len(get_parent) > 0:  # 確認有資料再進行
    getname = get_parent[0].find('div').text
else:
    print('抓不到資料，直接是空的')
    

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
    average_percentage = sum(percentages) / len(percentages)
    get_star_rate = round(average_percentage / 20, 2)

    
# 出售量    
if len(get_parent) > 2:
    div_tag = get_parent[2].find_all('div', class_='r6HknA uEPGHT')
    for j in div_tag:
        get_history_sold = j.text
        get_history_sold = get_history_sold.replace('已售出', '')
        get_history_sold = get_history_sold.replace(' ', '')

    
    
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


    

    
    

    

