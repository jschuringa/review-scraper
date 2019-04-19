import unittest
from unittest.mock import MagicMock
from app import app
from scraper.scraper import Scraper

class TestAppCases(unittest.TestCase):

    def test_url_is_restaurant_page_succeeds(self):
        """
            Asserts the endpoint succeeds when the url is a restaurant url
        """
        Scraper.get_scraper = MagicMock(return_value=Scraper([]))
        Scraper.get_reviews = MagicMock(return_value=[])
        with app.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 200)

    def test_url_is_reviews_page_succeeds(self):
        """
            Asserts the endpoint succeeds when the url is a restaurant review url
        """
        Scraper.get_scraper = MagicMock(return_value=Scraper([]))
        Scraper.get_reviews = MagicMock(return_value=[])
        with app.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727/reviews"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 200)

    def test_url_is_not_restaurant_or_reviews_page_fails(self):
        """
            Asserts the endpoint fails when the url is a not a restaurant or review url
        """
        with app.test_client() as client:
            sent = {"url": "www.google.com"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)

    def test_url_not_in_form_data_post(self):
        """
            Asserts the endpoint fails when the url is not in the form data
        """
        with app.test_client() as client:
            sent = {}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)

    def test_url_not_in_form_data_get(self):
        """
            Asserts the endpoint fails when the url is not in the form data
        """
        with app.test_client() as client:
            sent = {}
            result = client.get('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)

    def test_happy_path(self):
        """
           Asserts the endpoint returns a dictionary as json
        """
        reviewMockData = {"author": "test"}
        Scraper.get_scraper = MagicMock(return_value=Scraper([]))
        Scraper.get_reviews = MagicMock(return_value=[reviewMockData])
        with app.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            print(result)
            self.assertEqual(result.status_code, 200)
            