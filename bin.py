#! /anaconda2/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import send_me_email
import twitter_data

# Manually input keywords to keep abreast of
keyword_list = [('Insights', 'Alternative Data Insights'), ('Capital','Alternative Data capital'),('Financial','Alternative Data Financial'),('Research','Alternative Data Research'),('China','Alternative Data China'),('Careers','Alternative Data Careers'),('Company','Alternative Data Company'),('Services','Alternative Data Services'),('Dataset','Alternative Dataset')]
message = u''

# For each keyword, hit the twitter api to get matched tweet text and links to each tweet
for description, keyword in keyword_list:
    results = twitter_data.get_twitter_data(keyword = keyword, count = 50).to_html(index = False)
    message += u'{}:{}\n\n'.format(description, results)

subject = "Alt Data Sourcing Bot"
recipients = ["bemmerich@yipitdata.com", 'jkelly@yipitdata.com','mrondinaro@yipitdata.com']

# Send emails to all particpants in the project
for recipient in recipients:
    print recipient
    send_me_email.send_html_email(message, recipient, subject)
