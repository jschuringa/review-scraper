from datetime import datetime, timedelta, date
import re

class ReviewItem():
    def __init__(self, author, content, rating, date, top_reviewer, items_ordered, responded):
        self.author = author
        self.content = content
        self.rating = rating
        self.date = date
        self.top_reviewer = top_reviewer
        self.items_ordered = items_ordered
        self.responded = responded

    @staticmethod
    def parse_date(content):
        """
            Provides date string parsing specific to this type of ReviewItem
        """
        try:
            return datetime.strptime(content, "%b %d, %Y").date()
        except ValueError:
            pass
        if content == 'Today':
            return date.today()
        if content == 'Yesterday':
            return date.today() - timedelta(1)
        number_expr = re.compile("([0-9]*)")
        days_expr = re.compile("[0-9]\s(day(s)?)\s(ago)")
        if days_expr.match(content) is not None:
            days_past = int(number_expr.match(content)[0])
            return date.today() - timedelta(days_past)
        weeks_expr = re.compile("[0-9]\s(week(s)?)\s(ago)")
        if weeks_expr.match(content) is not None:
            days_past = int(number_expr.match(content)[0]) * 7
            return date.today() - timedelta(days_past)
        return content


    @staticmethod
    def build_review_item(html_item):
        """
            The constructor logic is too complex for the __init__, so we add a static method to handle it.
        """
        author = html_item.find("h6", {"class": "review-reviewer-name"}).contents[0]
        content = html_item.find("p", {"itemprop": "reviewBody"}).contents[0]
        rating = int(html_item.find("meta", {"itemprop": "ratingValue"})["content"])
        date = ReviewItem.parse_date(html_item.find("span", {"class": "meta-label"}).contents[0])
        top_reviewer = html_item.find("cb-icon", {"class": "review-topReviewerBadge"}) is not None
        responded = html_item.find("div", {"class": "review-response-restaurant"}) is not None
        items_ordered = []
        for menu_item in html_item.findAll("div", {"class": "review-ordered-item-title"}):
            items_ordered.append(menu_item.contents[0])
        return ReviewItem(author, content, rating, date, top_reviewer, items_ordered, responded)