from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv
from push import send_push_message

#there are these main chapters:
# 1. parse html
# 2. open the csv with already found wg's
# 3. overwrite the csv file and send messages via pushover

# 1 = Pushover; 2 = Telegram; 3 = None
use_notification = 1

#url with filter
myurl = "YOUR URL"

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

#test of output wg_list
#print(wg_list)

#######################################################

#list of already found wg's (csv)
url_list = []

#open csv with already listed wg's
filename_buffer = "wg-gesucht.csv"
b = open(filename_buffer, "r+")
url_csv = csv.reader(b, delimiter=';')

for url in url_csv:
    url_list.append(url[0])

b.close()

#test of output url_list
#print(url_list)

#######################################################

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
        #CHANGE APP_TOKEN
        
        if use_notification == 1:
            send_push_message("APP_TOKEN", "New WG found!", "https://www.wg-gesucht.de/" + wg)
        elif use_notification == 2:
            telegram_bot_sendtext("New WG found: " + wg)
        else:
            pass

#add already found wgs to add_list
for url in url_list:
    add_list.append(url)

#add items to csv
for item in add_list:
    b.write(item + "\n")

b.close()
