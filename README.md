# wg-gesucht_scraper
Scraper for searching a WG on wg-gesucht.de and notify via Pushover or Telegram bot

## Functions ##
After setting up the scraper it will search the predefined url (with your specific filter options) and give you an update via pushover or Telegram bot when new objects are being listed.

## Before use ##
Define your preferred way of notification under use_notification (main.py) and set your pushover user-token (push.py) & app-token (main.py) or your Telegram bot-token & bot-chatID (both in telegram.py) before use or there will be no notification. Also add your specific Search URL with the defined filters for your city (main.py).

**User-token (Pushover)**

![user_token_push](https://user-images.githubusercontent.com/55713049/71610831-b3357280-2b94-11ea-81d5-cef353d210fb.png)


**App-token (Pushover)**

![App_token_main](https://user-images.githubusercontent.com/55713049/71610794-50dc7200-2b94-11ea-92a1-7bd51e82f726.png)


**Bot-token & Bot-ChatID (Telegram)**

![Telegram_Options](https://user-images.githubusercontent.com/55713049/71761561-0d537200-2ecc-11ea-8502-1a41873ce030.png)


**URL**

![URL_main](https://user-images.githubusercontent.com/55713049/71610846-d829e580-2b94-11ea-9f29-a73e8e1a1909.png)


**ATTENTION** 

The scraper is using BeautifulSoup4, so you have to install it on your machine.

First install python3-pip with:

```
sudo apt-install python3-pip
```

And the Bs4 with:
```
pip3 install bs4
```

## Extra Information ##
If deployed on a server or raspberry-pi use a crontab to let it run in the background.
A good interval would be every 5 minutes.

```
crontab -e
```
And insert following crontab statement:
```
*/5 * * * * cd /your/path/to/script/wg-gesucht_scraper && exec python3 main.py
```
