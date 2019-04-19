import unittest
from unittest.mock import Mock, patch
from datetime import date, timedelta
from ..scraper import Scraper
from ..parser import ReviewItem
from .test_constants import test_html_default, test_html_with_response, test_html_top_reviewer, test_html_invalid

class TestScraperMethods(unittest.TestCase):

    def test_get_reviews_no_items(self):
        """
            Asserts a scraper with no item data does not create
            any garbage entries
        """
        scraper = Scraper([])
        result = scraper.get_reviews()
        self.assertEqual(len(result), 0)
    
    @patch("ReviewItem.build_review_item")
    def test_get_reviews(self):
        item1 = ReviewItem("me", "this is the first review", 2, date.today(), False, ["sandwich"], True)
        item2 = ReviewItem("you", "this is the second review", 4, date.today() - timedelta(1), True, ["chicken", "onion rings"], False)
        scraper = Scraper([1, 2])

