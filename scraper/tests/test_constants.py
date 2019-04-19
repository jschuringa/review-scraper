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

test_html_invalid = r'''
    <div>
        <h5 class="review-reviewer-name">Test Name</h5>
        <div itemprop="reviewBody">Test Content</div>
        <input itemprop="ratingValue" content="4" />
        <p class="meta-label">May 10, 2018</p>
    </div>
'''