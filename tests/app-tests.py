import unittest
from unittest.mock import MagicMock
from app import app
from scrapers.scraper import Scraper

class TestAppCases(unittest.TestCase):

    def test_url_is_restaurant_page_succeeds(self):
        Scraper.get_reviews = MagicMock(return_value=[])
        with app.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 200)

    def test_url_is_reviews_page_succeeds(self):
        Scraper.get_reviews = MagicMock(return_value=[])
        with app.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727/reviews"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 200)

    def test_url_is_not_restaurant_or_reviews_page_fails(self):
        with app.test_client() as client:
            sent = {"url": "www.google.com"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)