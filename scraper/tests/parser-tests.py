import unittest
from datetime import datetime, timedelta, date
from unittest.mock import MagicMock
from ..parser import ReviewItem

class TestParserMethods(unittest.TestCase):

    def test_parse_date_weeks(self):
        """
            Asserts that a date in the format of x weeks ago 
            is succesfully parsed
        """
        date = "2 weeks ago"
        result = ReviewItem.parse_date(date)
        expected = (datetime.today() - timedelta(14)).date()
        self.assertEquals(result, expected)

    def test_parse_date_week(self):
        """
            Asserts that a date in the format of x week ago 
            is succesfully parsed
        """
        date = "1 week ago"
        result = ReviewItem.parse_date(date)
        expected = (datetime.today() - timedelta(7)).date()
        self.assertEquals(result, expected)

    def test_parse_date_days(self):
        """
            Asserts that a date in the format of x days ago 
            is succesfully parsed
        """
        date = "2 days ago"
        result = ReviewItem.parse_date(date)
        expected = (datetime.today() - timedelta(2)).date()
        self.assertEquals(result, expected)

    def test_parse_date_day(self):
        """
            Asserts that a date in the format of x day ago 
            is succesfully parsed
        """
        date = "1 day ago"
        result = ReviewItem.parse_date(date)
        expected = (datetime.today() - timedelta(1)).date()
        self.assertEquals(result, expected)
