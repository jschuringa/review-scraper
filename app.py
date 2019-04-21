"""
    This module creates the flask application and defines the endpoints
"""

from urllib.parse import urlparse
import re
import json
from flask import Flask, request, jsonify
from scraper.scraper import Scraper

APP = Flask(__name__)

@APP.route("/scrape_reviews", methods=['POST'])
def get_reviews():
    """
        Accepts a url as form data and attempts to return review data as json
    """
    url = request.form['url']
    if url is None:
        data = {"success": False, "message": "Must provide a url to scrape reviews."}
        return APP.response_class(status=400, mimetype='applicaton/json', response=json.dumps(data))
    parsed_url = urlparse(url)
    main_page_expr = re.compile(r'\/(restaurant)\/(.*)\/([0-9]*)')
    review_page_expr = re.compile(r'\/(restaurant)\/(.*)\/([0-9]*)\/reviews')
    if parsed_url.netloc != "www.grubhub.com" or (main_page_expr.match(parsed_url.path) is None and review_page_expr.match(parsed_url.path) is None):
        data = {"success": False, "message": "Must be a grubhub restaurant or restaurant review page."}
        return APP.response_class(status=400, mimetype='applicaton/json', response=json.dumps(data))
    try:
        scraper = Scraper.get_scraper(url)
        return jsonify(scraper.get_reviews())
    except Exception as exception:
        data = {"success": False, "message": f"An unexpected error occured while scraping reviews: {exception}"}
        return APP.response_class(status=500, mimetype='applicaton/json', response=json.dumps(data))
