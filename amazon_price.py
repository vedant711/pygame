from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from twilio.rest import Client
import pywhatkit
# from selenium import webdriver
 

def search(search_text):

    url = f'https://www.amazon.in/s?k={search_text}&ref=nb_sb_noss_2&page='
    # url += '{}'
    return url

price = 'a-price'
offscreen = 'a-offscreen'

def record(item):
    try:
        price_parent = item.find('span',price)
        price_offscreen = price_parent.find('span',offscreen).text
    except AttributeError:
        return
    return price_offscreen

brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe"
options = webdriver.ChromeOptions()
options.headless = True
options.binary_location = brave_path
driver = webdriver.Chrome(executable_path='H:\Webmyne Internship\chromedriver.exe',options=options)
search_text = input('Enter the product to be searched: ')
prices = []
url = search(search_text)
for page in range(1,5):
    driver.get(url+str(page))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all("div", {"data-component-type": "s-search-result"})
    for item in results:
            record1 = record(item) #takes each item to extract_record() function above to get the prices
            if item:
                prices.append(record1)
# print(prices)
new_prices = []
single_price =''
for p in prices:
    # print(type(prices[0]))
    # p=p[1:]
    if p != None:
        p1 = str(p)
        p = str(p1).replace('₹','').replace(',','')
    # for i in len((p)):
    #     if p[i].isdigit():
    #         single_price+=p[i]
    # print(p)
        if p.isdigit() and int(p) <= 100000:
            new_prices.append(int(p))
print(new_prices)

# auth_token = ''
# account_sid=''
# client = Client(account_sid,auth_token)
# client.messages.create(

# # To send SMS to mobile phone

# to="+917874822586", # Your phone number, don’t forget to add the country code. This should be hidden

# from_="+15106500813", # Your Twilio phone number. This should be hidden

# body=f"There are {len(new_prices)} Macbook within budget, ₹100000" # message that will be sent to your mobile phone

# )


pywhatkit.sendwhatmsg_to_group("IabiTeinsJJ0So4MbpNUrb",f"There are {len(new_prices)} Macbook within budget, ₹100000", 16, 48)