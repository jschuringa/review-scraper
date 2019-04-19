from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .parser import ReviewItem


class Scraper():

    def __init__(self, items):
        self.items = items

    @staticmethod
    def get_scraper(url):
        """
        Builds a new grubhub scraper scraper object by getting the html for review items. Initializes a full window version of the chrome driver
        to avoid bot detection on grubhub.
        """
        options = Options()
        user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        driver.maximize_window()
        soup = BeautifulSoup(driver.page_source, "html5lib")
        driver.close()
        items = soup.findAll("div", {"class": "review-wrapper"})
        return Scraper(items)
    
    def get_reviews(self):
        """
            Utilizes the review item static method to build a list of reviews from html review items.
        """
        reviews = []
        for item in self.items:
            reviews.append(ReviewItem.build_review_item(item).__dict__)
        return reviews

