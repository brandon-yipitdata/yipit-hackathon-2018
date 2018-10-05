#! /anaconda2/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import private
import settings
import web

api = twitter.Api(
    consumer_key = private.CONSUMER_KEY,
    consumer_secret = private.CONSUMER_SECRET,
    access_token_key = private.ACCESS_TOKEN_KEY,
    access_token_secret = private.ACCESS_TOKEN_SECRET
    )

empty_list = []
for description, keyword in settings.LIST_KEYWORDS:
    results = web.get_twitter_data(keyword = keyword, count = 100)
    empty_list.append(results)

pd.set_option('max_colwidth', 280)
df = pd.concat(empty_list)

subject = "Alt Data Sourcing Bot"
message = u'Your Alt Data Directory!\n\n{}'.format(df.to_html(index = False))

for recipient in private.EMAIL_RECIPIENTS:
    print recipient
    web.send_html_email(message, recipient, subject)
