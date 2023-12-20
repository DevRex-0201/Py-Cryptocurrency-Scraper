import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Spreadsheet by title
sheet_url = "https://docs.google.com/spreadsheets/d/1MUAZ2SH8jrIkczJ9rPwxHZ9lyuQ5fR2kSQZ9T3BRIeY/edit?usp=sharing"
spreadsheet = client.open_by_url(sheet_url)

# Get the worksheet by name
worksheet_name = "Sheet1"
worksheet = spreadsheet.get_worksheet(0)

# If the worksheet is not found, create a new one
if worksheet is None:
    worksheet = spreadsheet.add_worksheet(title=worksheet_name, rows="100", cols="20")  # Adjust rows and cols accordingly

# Define the header names
header_names = ["Coin Name", "URL", "Website", "Whitepaper", "GitHub", "Discord", "Telegram"]

# Check if the worksheet is empty (no header row) and add headers if needed
existing_headers = worksheet.row_values(1)
if not existing_headers:
    worksheet.insert_row(header_names, index=1)

urls = ["https://coinmarketcap.com/?page=1"]
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
        worksheet.append_row(coin_data)
    
    else:
        print(f"Error: Failed to retrieve the page. Status code: {response_coin.status_code}")

for url in urls:
    scrape_currencies(url)
    

    
