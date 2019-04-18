from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scraper():

    @staticmethod
    def get_reviews(url):
        options = Options()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        driver.maximize_window()
        soup = BeautifulSoup(driver.page_source, "html5lib")
        print(soup)
        items = soup.findAll("div", {"class": "review-wrapper"})
        print(items)
        return items