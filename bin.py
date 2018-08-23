import pandas as pd
import send_me_email
import twitter_data

use_case = twitter_data.get_twitter_data(keyword = 'Alt Data Use Case', count = 100)

subject = "Hackathon"
recipient = "bemmerich@yipitdata.com"
message = u'This is your data:{}'.format(use_case.to_html(index = False))

send_me_email.send_html_email(message, recipient, subject)

import ipdb; ipdb.set_trace()
