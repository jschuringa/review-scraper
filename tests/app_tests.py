"""
    Provides tests for the app module
"""

import unittest
from unittest.mock import MagicMock, patch
from app import APP
from scraper.scraper import Scraper

class TestAppCases(unittest.TestCase):
    """
        Tests methods and error responses for the app module
    """

    def test_url_is_restaurant_page_succeeds(self):
        """
            Asserts the endpoint succeeds when the url is a restaurant url
        """
        Scraper.get_scraper = MagicMock(return_value=Scraper([]))
        Scraper.get_reviews = MagicMock(return_value=[])
        with APP.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 200)

    def test_url_is_not_restaurant_page_fails(self):
        """
            Asserts the endpoint fails when the url is a not a restaurant or review url
        """
        with APP.test_client() as client:
            sent = {"url": "www.google.com"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)

    def test_url_not_in_form_data_post(self):
        """
            Asserts the endpoint fails when the url is not in the form data
        """
        with APP.test_client() as client:
            sent = {}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 400)

    @patch("scraper.scraper.Scraper.get_reviews")
    def test_scraper_errors(self, scraper_mock):
        """
            Asserts internal server error captured and returned
        """
        scraper_mock.side_effect = KeyError()
        with APP.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            self.assertEqual(result.status_code, 500)

    def test_happy_path(self):
        """
           Asserts the endpoint returns a dictionary as json
        """
        reviewMockData = {"author": "test"}
        Scraper.get_scraper = MagicMock(return_value=Scraper([]))
        Scraper.get_reviews = MagicMock(return_value=[reviewMockData])
        with APP.test_client() as client:
            sent = {"url": "https://www.grubhub.com/restaurant/hashbrowns-on-wells-1155-n-wells-st-chicago/287727"}
            result = client.post('/scrape_reviews', data=sent)
            print(result)
            self.assertEqual(result.status_code, 200)
            