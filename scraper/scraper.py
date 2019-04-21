"""
    This module contains the logic for accessing a web page with selenium and building a scraper class based off of it.
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from scraper.parser import ReviewItem

class Scraper():
    """
        This class handles getting a new scraper through a static constructor method and building the review items into dictionaries
    """

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
        all_reviews_button = driver.find_element_by_id("allReviewsPage")
        if all_reviews_button is not None:
            all_reviews_button.click()
            # sleeping is not my favorite solution but the page wasn't loading fast enough
            time.sleep(5)
        while True:
            try:
                see_more_button = driver.find_element_by_xpath('//button[@at-allreviews-seemore="true"]')
                see_more_button.click()
            except NoSuchElementException:
                break
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
