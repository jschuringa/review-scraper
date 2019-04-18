import requests
from bs4 import BeautifulSoup
from selenium import webdriver


class Scraper():

    @staticmethod
    def get_reviews(url):
        driver = webdriver.Firefox()
        driver.get(url)
        print(response)
        soup = BeautifulSoup(driver.page_source, "html5lib")
        print(soup)
        items = soup.findAll("div", {"class": "review-wrapper"})
        print(items)
        return items