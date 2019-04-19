from flask import Flask, request, jsonify
from urllib.parse import urlparse
import re
import json
from scraper.scraper import Scraper

app = Flask(__name__)

@app.route("/scrape_reviews", methods=['GET', 'POST'])
def get_reviews():
    url = request.form['url']
    if url is None:
        data = {"success": False, "message": "Must provide a url to scrape reviews."}
        return app.response_class(status=400, mimetype='applicaton/json', response=json.dumps(data))   
    parsed_url = urlparse(url)
    main_page_expr = re.compile('\/(restaurant)\/(.*)\/([0-9]*)')
    review_page_expr = re.compile('\/(restaurant)\/(.*)\/([0-9]*)\/reviews')
    if parsed_url.netloc != "www.grubhub.com" or (main_page_expr.match(parsed_url.path) is None and review_page_expr.match(parsed_url.path) is None):
        data = {"success": False, "message": "Must be a grubhub restaurant or restaurant review page."}
        return app.response_class(status=400, mimetype='applicaton/json', response=json.dumps(data))    
    try:
        scraper = Scraper.get_scraper(url)
        return jsonify(scraper.get_reviews())
    except Exception as e:
        data = {"success": False, "message": f"An unexpected error occured while scraping reviews: {e}"}
        return app.response_class(status=500, mimetype='applicaton/json', response=json.dumps(data))