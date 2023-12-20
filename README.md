# Cryptocurrency Data Scraper

## Overview
This Python script is designed to scrape cryptocurrency data from CoinMarketCap and populate a Google Spreadsheet with relevant information. It utilizes web scraping techniques with the BeautifulSoup library to extract details such as coin name, URLs, website, whitepaper, GitHub, Discord, and Telegram links.

## Dependencies
Ensure you have the necessary libraries installed using the following:
```bash
pip install requests
pip install beautifulsoup4
pip install gspread oauth2client
```

## Google Sheets Integration
To use the Google Sheets functionality, you need to set up a service account and obtain the `credentials.json` file. Refer to the [Google Sheets API documentation](https://developers.google.com/sheets/api/guides/authorizing) for instructions on obtaining these credentials.

## Configuration
1. Set the appropriate scope in the `scope` variable.
2. Provide the path to your `credentials.json` file.
3. Adjust the `sheet_url` and `worksheet_name` according to your Google Spreadsheet.

## Execution
Run the script, and it will scrape cryptocurrency data from multiple pages on CoinMarketCap, extracting information for each coin and adding it to the specified Google Spreadsheet.

## Customization
- You can customize the `urls` list to include specific pages from CoinMarketCap.
- Modify the `header_names` list to change the column headers in the Google Spreadsheet.

## Note
- Be mindful of web scraping ethics and adhere to the terms of service of the websites you are scraping.
- Adjust the script according to any changes in the HTML structure of the CoinMarketCap website.

## Disclaimer
This script is provided as-is and may require updates based on changes to external websites or libraries. Use it responsibly and in compliance with relevant terms and conditions.