import csv
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_ad(element):
    # Check if the element is marked as an ad (unchanged)
    ad_labels = element.find_elements(By.CSS_SELECTOR, ".ad-icon")
    if ad_labels:
        return True

    url = element.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    if "googleadservices.com" in url or "google.com/ads" in url:
        return True

    return False


def find_contact_page_link(driver):
    # Get all links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    # Keywords that are commonly used for contact page links
    contact_keywords = ["contact", "get in touch", "reach us", "support", "help", "about us", "contact us",
                        "contactez nous"]

    # Search for links that contain any of the contact keywords
    for link in links:
        link_text = link.text.strip().lower()
        for keyword in contact_keywords:
            if keyword in link_text:
                return link

    return None


def scrape_google_results(search_query, driver):
    driver.get(f"https://www.google.com/search?q={search_query}")

    search_results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")

    organic_results = [result for result in search_results if not is_ad(result)]

    if organic_results:
        link = organic_results[0].find_element(By.CSS_SELECTOR, "a")
        link.click()

        # Wait for the new page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

        # Find the link to the contact page
        contact_page_link = find_contact_page_link(driver)
        if contact_page_link:
            contact_page_link.click()

            # Wait for the contact page to fully load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

            contact_page_html = driver.page_source
            soup = BeautifulSoup(contact_page_html, 'html.parser')

            # Extract phone numbers using regular expressions
            phone_numbers = []
            phone_regex = re.compile(r'[\+()]?[1-9][0-9 .()-]{8,}[0-9]')
            for text in soup.stripped_strings:
                for match in phone_regex.findall(text):
                    phone_numbers.append(match)

            # Extract email addresses using regular expressions
            email_addresses = []
            email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
            for text in soup.stripped_strings:
                for match in email_regex.findall(text):
                    email_addresses.append(match)

            return driver.current_url, contact_page_link.get_attribute("href"), phone_numbers, email_addresses

    return None, None, [], []


def main():
    input_file = "companies.csv"
    output_file = "output.csv"

    with open(input_file, newline='', encoding='utf-8') as csvfile, open(output_file, 'w', newline='',
                                                                         encoding='utf-8') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile)

        driver = webdriver.Chrome()

        for row in reader:
            company_name = row[0].strip()
            website_url, contact_page_url, phone_numbers, email_addresses = scrape_google_results(company_name, driver)

            writer.writerow([company_name, website_url, contact_page_url, phone_numbers, email_addresses])

            # Rate limiting to avoid overloading the server
            time.sleep(10)

        driver.quit()


if __name__ == "__main__":
    main()
