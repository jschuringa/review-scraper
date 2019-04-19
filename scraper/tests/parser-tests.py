import unittest
from datetime import datetime, timedelta, date
from unittest.mock import MagicMock
from bs4 import BeautifulSoup
from ..parser import ReviewItem

class TestParserMethods(unittest.TestCase):

    test_html_default = r'''
        <div>
            <h6 class="review-reviewer-name">Test Name</h6>
            <p itemprop="reviewBody">Test Content</p>
            <meta itemprop="ratingValue" content="4" />
            <span class="meta-label">May 10, 2018</span>
            <div id="menuItems">
                <div class="review-ordered-item-title">Test Food</div>
            </div>
        </div>
    '''

    test_html_with_response = r'''
        <div>
            <h6 class="review-reviewer-name">Test Name</h6>
            <p itemprop="reviewBody">Test Content</p>
            <meta itemprop="ratingValue" content="4" />
            <span class="meta-label">May 10, 2018</span>
            <div id="menuItems">
                <div class="review-ordered-item-title">Test Food</div>
            </div>
            <div class="review-response-restaurant">test response</div>
        </div>
    '''

    test_html_top_reviewer = r'''
        <div>
            <h6 class="review-reviewer-name">Test Name</h6>
            <p itemprop="reviewBody">Test Content</p>
            <meta itemprop="ratingValue" content="4" />
            <span class="meta-label">May 10, 2018</span>
            <div id="menuItems">
                <div class="review-ordered-item-title">Test Food</div>
            </div>
            <cb-icon class="review-topReviewerBadge"/>
        </div>
    '''

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

    def test_build_review_item_default(self):


