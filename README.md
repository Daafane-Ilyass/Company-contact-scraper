# Company Contact Page Scraper


This Python script allows you to scrape contact information from Google search results for a list of companies provided in a CSV file.

## Prerequisites

Before running the script, you need to have the following installed on your system:

1. Python 3.x: The script is written in Python, so you'll need to have Python 3.x installed. You can download Python from the official website: https://www.python.org/downloads/

2. Chrome Web Browser: The script uses the Chrome browser for automated web scraping. If you don't have Chrome installed, you can download it from: https://www.google.com/chrome/

3. ChromeDriver: ChromeDriver is required for Selenium to interact with the Chrome browser. Make sure you download the appropriate version of ChromeDriver that matches your installed Chrome browser version. You can download ChromeDriver from: https://sites.google.com/a/chromium.org/chromedriver/downloads

   After downloading ChromeDriver, place it in a directory that is in your system's PATH environment variable.

## Python Dependencies

The script relies on the following Python packages, which need to be installed before running the script:

- Selenium: It is used for automating the browser interactions with Chrome. Install it using:

```bash
pip install selenium
```

- BeautifulSoup4: This library is used for parsing the HTML content of web pages. Install it using:

```bash
pip install beautifulsoup4
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Daafane-Ilyass/Company-contact-scraper.git
cd Company-contact-scraper
```

2. Create a CSV file named `companies.csv` in the root directory with the list of company names you want to search for. The first column of the CSV should contain the company names.

3. Make sure you have installed the required Python packages (Selenium and BeautifulSoup4) as mentioned above.

4. Ensure that you have Chrome and ChromeDriver installed on your system.

5. Run the script:

```bash
python scrap.py
```

6. The script will search Google for each company name, find the most relevant organic search result, and navigate to the website's contact page (if available). It will then scrape phone numbers and email addresses from that page. The results will be saved to a new CSV file named `output.csv` in the root directory.

## Notes

- The script uses Selenium with ChromeDriver to automate the process, so it requires Chrome to be installed on your system.

- The script implements basic rate-limiting with a 2-second delay between each search to avoid overloading the server.

- The contact page is identified by common keywords like "contact," "support," etc., in the link text.

- The phone numbers and email addresses are extracted using regular expressions from the HTML content of the contact page.

- Ensure that you have a good internet connection as the script needs to access Google search results.

## Disclaimer

Please be mindful of any legal or ethical considerations while using this script. Web scraping may be against the terms of service of certain websites, and it's essential to respect the website's policies and guidelines. Use this script responsibly and only for legitimate purposes.
