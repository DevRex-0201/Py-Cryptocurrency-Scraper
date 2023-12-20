import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = ["https://coinmarketcap.com/?page=1", "https://coinmarketcap.com/?page=2", "https://coinmarketcap.com/?page=3", "https://coinmarketcap.com/?page=4", "https://coinmarketcap.com/?page=5", "https://coinmarketcap.com/?page=6", "https://coinmarketcap.com/?page=7", "https://coinmarketcap.com/?page=8", "https://coinmarketcap.com/?page=9", "https://coinmarketcap.com/?page=10", "https://coinmarketcap.com/?page=11", "https://coinmarketcap.com/?page=12", "https://coinmarketcap.com/?page=13", "https://coinmarketcap.com/?page=14", "https://coinmarketcap.com/?page=15", "https://coinmarketcap.com/?page=16", "https://coinmarketcap.com/?page=17", "https://coinmarketcap.com/?page=18", "https://coinmarketcap.com/?page=19", "https://coinmarketcap.com/?page=20", "https://coinmarketcap.com/?page=21", "https://coinmarketcap.com/?page=22", "https://coinmarketcap.com/?page=23", "https://coinmarketcap.com/?page=24", "https://coinmarketcap.com/?page=25", "https://coinmarketcap.com/?page=26", "https://coinmarketcap.com/?page=27", "https://coinmarketcap.com/?page=28", "https://coinmarketcap.com/?page=29", "https://coinmarketcap.com/?page=30", "https://coinmarketcap.com/?page=31", "https://coinmarketcap.com/?page=32", "https://coinmarketcap.com/?page=33", "https://coinmarketcap.com/?page=34", "https://coinmarketcap.com/?page=35", "https://coinmarketcap.com/?page=36", "https://coinmarketcap.com/?page=37", "https://coinmarketcap.com/?page=38", "https://coinmarketcap.com/?page=39", "https://coinmarketcap.com/?page=40", "https://coinmarketcap.com/?page=41", "https://coinmarketcap.com/?page=42", "https://coinmarketcap.com/?page=43", "https://coinmarketcap.com/?page=44", "https://coinmarketcap.com/?page=45", "https://coinmarketcap.com/?page=46", "https://coinmarketcap.com/?page=47", "https://coinmarketcap.com/?page=48", "https://coinmarketcap.com/?page=49", "https://coinmarketcap.com/?page=50", "https://coinmarketcap.com/?page=51", "https://coinmarketcap.com/?page=52", "https://coinmarketcap.com/?page=53", "https://coinmarketcap.com/?page=54", "https://coinmarketcap.com/?page=55", "https://coinmarketcap.com/?page=56", "https://coinmarketcap.com/?page=57", "https://coinmarketcap.com/?page=58", "https://coinmarketcap.com/?page=59", "https://coinmarketcap.com/?page=60", "https://coinmarketcap.com/?page=61", "https://coinmarketcap.com/?page=62", "https://coinmarketcap.com/?page=63", "https://coinmarketcap.com/?page=64", "https://coinmarketcap.com/?page=65", "https://coinmarketcap.com/?page=66", "https://coinmarketcap.com/?page=67", "https://coinmarketcap.com/?page=68", "https://coinmarketcap.com/?page=69", "https://coinmarketcap.com/?page=70", "https://coinmarketcap.com/?page=71", "https://coinmarketcap.com/?page=72", "https://coinmarketcap.com/?page=73", "https://coinmarketcap.com/?page=74", "https://coinmarketcap.com/?page=75", "https://coinmarketcap.com/?page=76", "https://coinmarketcap.com/?page=77", "https://coinmarketcap.com/?page=78", "https://coinmarketcap.com/?page=79", "https://coinmarketcap.com/?page=80", "https://coinmarketcap.com/?page=81", "https://coinmarketcap.com/?page=82", "https://coinmarketcap.com/?page=83", "https://coinmarketcap.com/?page=84", "https://coinmarketcap.com/?page=85", "https://coinmarketcap.com/?page=86", "https://coinmarketcap.com/?page=87", "https://coinmarketcap.com/?page=88", "https://coinmarketcap.com/?page=89", "https://coinmarketcap.com/?page=90"]
scraped_links = []
scraped_data = []
num = 0

def scrape_currencies(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <a> elements with "currencies" in the "href" attribute
        tr_elements = soup.find_all('tr')

        # Extract and print the "href" values of the found <a> elements
        for element in tr_elements:
            td_elements = element.find_all('td')
            if len(td_elements) > 2:
                href_value = "https://coinmarketcap.com" + td_elements[2].find('a').get('href')
                # print(href_value)
                scrape_currency_data(href_value)
                # scraped_links.append(href_value)
            else:
                print("No third td element found in the row.")
        
def scrape_currency_data(url_coin):
    global num  # Declare num as a global variable

    # Send a GET request to the specified URL
    response_coin = requests.get(url_coin)

    # Check if the request was successful (status code 200)
    if response_coin.status_code == 200:
        # Parse the HTML content of the page
        soup_coin = BeautifulSoup(response_coin.content, 'html.parser')
        link_elements = soup_coin.find_all(attrs={"rel": "nofollow noopener"})
        coin_name = soup_coin.find(attrs={"data-role": "coin-name"}).get_text().replace(' price', '')
        website_link = ''
        whitepaper_link = ''
        github_link = ''
        discord_link = ''
        telegram_link = ''

        for link in link_elements:
            if 'Website' in link.get_text():
                website_link = link['href']
            elif 'Whitepaper' in link.get_text():
                whitepaper_link = link['href']
            elif 'GitHub' in link.get_text():
                github_link = link['href']
            elif 'Discord' in link.get_text():
                discord_link = link['href']
            elif 'Telegram' in link.get_text():
                telegram_link = link['href']

        # Print or use the links outside the loop
        print('\n')
        print("CoinUrl:", url_coin)
        print("Website:", website_link)
        print("Whitepaper:", whitepaper_link)
        print("GitHub:", github_link)
        print("Discord:", discord_link)
        print("Telegram:", telegram_link)
        
        coin_data = [coin_name, url_coin, website_link, whitepaper_link, github_link, discord_link, telegram_link]
        scraped_data.append(coin_data)
    
    else:
        print(f"Error: Failed to retrieve the page. Status code: {response_coin.status_code}")

for url in urls:
    scrape_currencies(url)
    
# Create a DataFrame from the list
df = pd.DataFrame(scraped_data, columns=["Coin Name", "URL", "Website", "Whitepaper", "GitHub", "Discord", "Telegram"])

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
    