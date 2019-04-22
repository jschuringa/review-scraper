"""
    This module contains the logic for accessing a web page with selenium and building a scraper class based off of it.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import ui
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
        wait = ui.WebDriverWait(driver, 5)
        driver.maximize_window()
        try:
            wait.until(lambda driver: driver.find_element_by_id("allReviewsPage"))
            driver.find_element_by_id("allReviewsPage").click()
            wait.until(lambda driver: driver.find_element_by_xpath('//button[@at-allreviews-seemore="true"]'))
            while True:
                try:
                    see_more_button = driver.find_element_by_xpath('//button[@at-allreviews-seemore="true"]')
                    see_more_button.click()
                except NoSuchElementException:
                    # This exception will eventually be triggered once the page is done handling loading all the reviews
                    # as the Load More button will stop rendering.
                    break
        except TimeoutException:
            # This exception will be triggered either when the restaurant page has too few reviews for a reviews page, or the reviews page we
            # navigated to doesn't need to have the all reviews button clicked immediately after navigating to it
            pass
        except:
            driver.close()
            raise
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
