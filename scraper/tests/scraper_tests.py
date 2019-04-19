import unittest
from ..scraper import Scraper

class TestScraperMethods(unittest.TestCase):

    def test_get_reviews_no_items(self):
        scraper = Scraper([])
        result = scraper.get_reviews()
        self.assertEqual(len(result), 0)