import configparser
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
from push import send_push_message
from telegram import telegram_bot_sendtext

#CHANGE THIS URL!
myurl = ""


#read the config.txt
config = configparser.ConfigParser()
config.read_file(open(r'config.txt'))
use_notification = config.get('Basic-Configuration', 'use_notification')
use_notification = int(use_notification)
user_token = config.get('Pushover', 'user_token')
app_token = config.get('Pushover', 'app_token')
bot_token = config.get('Telegram', 'bot_token')
bot_chatID = config.get('Telegram', 'bot_chatID')



#read the html of the website
uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each wg
wg_ads = page_soup.findAll("h4", {"class":"headline headline-list-view truncate_title"})

#list to test against
wg_list = []

#parse url out of wg_ads
for wg_ad in wg_ads:
    wg_ad = wg_ad.a["href"]
    wg_list.append(wg_ad)



#list of already found wg's (csv)
url_list = []

#open csv with already listed wg's
filename_buffer = "wg-gesucht.csv"
b = open(filename_buffer, "r+")
url_csv = csv.reader(b, delimiter=';')

for url in url_csv:
    url_list.append(url[0])

b.close()



#overwrite the csv
filename_buffer = "wg-gesucht.csv"
b = open(filename_buffer, "w")

#list to add
add_list = []

#cycle through list and check
for wg in wg_list:
    if wg in url_list:
        print("do nothing...")
    else:
        print(wg)
        add_list.append(wg)

        if use_notification == 1:
            send_push_message(user_token, app_token, "New WG found!", "https://www.wg-gesucht.de/" + wg)
        elif use_notification == 2:
            telegram_bot_sendtext(bot_token, bot_chatID, "New WG found: https://www.wg-gesucht.de/" + wg)
        elif use_notification == 3:
            send_push_message(user_token, app_token, "New WG found!", "https://www.wg-gesucht.de/" + wg)
            telegram_bot_sendtext(bot_token, bot_chatID, "New WG found: https://www.wg-gesucht.de/" + wg)
        elif use_notification == 4:
            continue

#add already found wgs to add_list
for url in url_list:
    add_list.append(url)

#add items to csv
for item in add_list:
    b.write(item + "\n")

b.close()
