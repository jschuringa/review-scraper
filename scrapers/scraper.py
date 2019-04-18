from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper():

    @staticmethod
    def get_reviews(url):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html5lib")
        print(soup)
        items = soup.findAll("div", {"class": "review-wrapper"})
        print(items)
        return items