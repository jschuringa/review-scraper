"""
    Provides tests and test infrastructure for the parser class
"""

import unittest
from datetime import datetime, timedelta, date
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
from scraper.parser import ReviewItem
from .test_constants import test_html_default, test_html_with_response, test_html_top_reviewer, test_html_invalid, raise_index_error

class TestParserMethods(unittest.TestCase):
    """
        Tests methods in the parser module
    """

    def test_parse_date_today(self):
        """
            Asserts that a date in the format of Today
            is succesfully parsed
        """
        content = "Today"
        result = ReviewItem.parse_date(content)
        expected = date.today()
        self.assertEqual(result, expected)

    def test_parse_date_yesterday(self):
        """
            Asserts that a date in the format of Yesterday
            is succesfully parsed
        """
        content = "Yesterday"
        result = ReviewItem.parse_date(content)
        expected = (datetime.today() - timedelta(1)).date()
        self.assertEqual(result, expected)

    def test_parse_date_weeks(self):
        """
            Asserts that a date in the format of x weeks ago 
            is succesfully parsed
        """
        content = "2 weeks ago"
        result = ReviewItem.parse_date(content)
        expected = (datetime.today() - timedelta(14)).date()
        self.assertEqual(result, expected)

    def test_parse_date_week(self):
        """
            Asserts that a date in the format of x week ago 
            is succesfully parsed
        """
        content = "1 week ago"
        result = ReviewItem.parse_date(content)
        expected = (datetime.today() - timedelta(7)).date()
        self.assertEqual(result, expected)

    def test_parse_date_days(self):
        """
            Asserts that a date in the format of x days ago 
            is succesfully parsed
        """
        content = "2 days ago"
        result = ReviewItem.parse_date(content)
        expected = (datetime.today() - timedelta(2)).date()
        self.assertEqual(result, expected)

    def test_parse_date_day(self):
        """
            Asserts that a date in the format of x day ago 
            is succesfully parsed
        """
        content = "1 day ago"
        result = ReviewItem.parse_date(content)
        expected = (datetime.today() - timedelta(1)).date()
        self.assertEqual(result, expected)

    @patch("scraper.parser.datetime")
    def test_parse_date_unexpected_exception(self, datetime_mock):
        """
            Asserts that an unexpected error gets propagated through and not caught
            in the parse date method
        """
        datetime_mock.strptime = raise_index_error
        content = "anything"
        self.assertRaises(IndexError, ReviewItem.parse_date, content)

    def test_build_review_item_default(self):
        """
            Asserts that the expected fields are parsed correctly
            with no response or top reviewer
        """
        soup = BeautifulSoup(test_html_default, "html5lib")
        result = ReviewItem.build_review_item(soup)
        self.assertEqual(result.author, "Test Name")
        self.assertEqual(result.content, "Test Content")
        self.assertEqual(result.rating, 4)
        self.assertTrue(isinstance(result.review_date, date))
        self.assertFalse(result.responded)
        self.assertFalse(result.top_reviewer)
        self.assertEqual(len(result.items_ordered), 1)

    def test_build_review_item_top_reviewer(self):
        """
            Asserts that the expected fields are parsed correctly
            for a top reviewer
        """
        soup = BeautifulSoup(test_html_top_reviewer, "html5lib")
        result = ReviewItem.build_review_item(soup)
        self.assertEqual(result.author, "Test Name")
        self.assertEqual(result.content, "Test Content")
        self.assertEqual(result.rating, 4)
        self.assertTrue(isinstance(result.review_date, date))
        self.assertFalse(result.responded)
        self.assertTrue(result.top_reviewer)
        self.assertEqual(len(result.items_ordered), 1)

    def test_build_review_item_response(self):
        """
            Asserts that the expected fields are parsed correctly
            with a response
        """
        soup = BeautifulSoup(test_html_with_response, "html5lib")
        result = ReviewItem.build_review_item(soup)
        self.assertEqual(result.author, "Test Name")
        self.assertEqual(result.content, "Test Content")
        self.assertEqual(result.rating, 4)
        self.assertTrue(isinstance(result.review_date, date))
        self.assertTrue(result.responded)
        self.assertFalse(result.top_reviewer)
        self.assertEqual(len(result.items_ordered), 1)
    
    def test_build_review_item_invalid_html(self):
        """
            Asserts that the constructor raises an exception
            when incorrectly formatted html is passed in
        """
        soup = BeautifulSoup(test_html_invalid, "html5lib")
        self.assertRaises(AttributeError, ReviewItem.build_review_item, soup)

