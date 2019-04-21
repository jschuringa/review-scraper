"""
    Provides tests for the scraper module
"""

import unittest
from unittest.mock import Mock, patch
from datetime import date, timedelta
from scraper import scraper
from scraper import parser
from .test_constants import test_html_default, test_html_with_response, test_html_top_reviewer, test_html_invalid

class TestScraperMethods(unittest.TestCase):
    """
        Tests the methods in the scraper class
    """

    def test_get_reviews_no_items(self):
        """
            Asserts a scraper with no item data does not create
            any garbage entries
        """
        test_scraper = scraper.Scraper([])
        result = test_scraper.get_reviews()
        self.assertEqual(len(result), 0)
    
    @patch("scraper.parser.ReviewItem.build_review_item")
    def test_get_reviews(self, mock_build):
        """
            Asserts get_reviews builds the correct data structure
        """
        item1 = parser.ReviewItem("me", "this is the first review", 2, date.today(), False, ["sandwich"], True)
        item2 = parser.ReviewItem("you", "this is the second review", 4, date.today() - timedelta(1), True, ["chicken", "onion rings"], False)
        mock_build.side_effect = [item1, item2]
        test_scraper = scraper.Scraper([1, 2])
        result = test_scraper.get_reviews()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], item1.__dict__)
        self.assertEqual(result[1], item2.__dict__)

