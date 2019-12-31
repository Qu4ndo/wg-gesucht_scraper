# wg-gesucht_scraper
Scraper for searching a WG on wg-gesucht.de

## Functions ##
After setting up the scraper it will search the predefined url (with your specific filter options) and give you an update via pushover when new objects are being listed.

## Before use ##
Define your pushover user token (push.py) and your app-token (main.py) before use or there will be no notification. Also add your specific Search URL with the defined filters for your city (main.py).

**User token**

![user_token_push](https://user-images.githubusercontent.com/55713049/71610831-b3357280-2b94-11ea-81d5-cef353d210fb.png)


**App token**

![App_token_main](https://user-images.githubusercontent.com/55713049/71610794-50dc7200-2b94-11ea-92a1-7bd51e82f726.png)


**URL**

![URL_main](https://user-images.githubusercontent.com/55713049/71610846-d829e580-2b94-11ea-9f29-a73e8e1a1909.png)


## Extra Information ##
If deployed on a server or raspberry-pi use a crontab to let it run in the background.
A good interval would be every 5 minutes.

```
crontab -e
```
And insert following crontab statement:
```
*/5 * * * * python3 /your/path/to/script/wg-gesucht_scraper/main.py
```
