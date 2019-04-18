from flask import Flask, request, jsonify
from urllib.parse import urlparse
import re
import json
from scrapers.scraper import Scraper

app = Flask(__name__)

@app.route("/scrape_reviews", methods=['POST'])
def get_reviews():
    url = request.form['url']
    parsed_url = urlparse(url)
    main_page_expr = re.compile('\/(restaurant)\/(.*)\/([0-9]*)')
    review_page_expr = re.compile('\/(restaurant)\/(.*)\/([0-9]*)\/reviews')
    if parsed_url.netloc != "www.grubhub.com" or (main_page_expr.match(parsed_url.path) is None and review_page_expr.match(parsed_url.path) is None):
        data = {"success": False, "message": "Must be a grubhub restaurant or restaurant review page."}
        return app.response_class(status=400, mimetype='applicaton/json', response=json.dumps(data))

        #return jsonify(success=False, message="Must be a grubhub restaurant or restaurant review page.", status_code=400)
    
    try:
        return jsonify(Scraper.get_reviews(url))
    except Exception as e:
        return jsonify(success=False, status_code=500, messasge=f"An unexpected error occured while scraping reviews: {e}")
        
    
    return jsonify(success=True)