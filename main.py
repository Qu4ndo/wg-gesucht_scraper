from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import csv

#url with filter
myurl = "https://www.wg-gesucht.de/wg-zimmer-in-Innsbruck.161.0.1.0.html?offer_filter=1&noDeact=1&city_id=161&category=0&rent_type=2&rMax=550&ot%5B%5D=3053&ot%5B%5D=3050&ot%5B%5D=3052&ot%5B%5D=3051&wgSea=2&wgAge=22"

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each wg
wg_ads = page_soup.findAll("h4", {"class":"headline headline-list-view truncate_title"})

#list to test against
wg_list = []

for wg_ad in wg_ads:
    wg_ad = wg_ad.a["href"]
    wg_list.append(wg_ad)

print(wg_list)
