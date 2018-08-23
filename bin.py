import pandas as pd
import send_me_email
import twitter_data

alt_data = twitter_data.get_twitter_data(keyword = 'Alternative Data', count = 50).to_html(index = False)
sat_data = twitter_data.get_twitter_data(keyword = 'Satellite Data', count = 50).to_html(index = False)


subject = "Alt Data Sourcing Bot"
recipients = ["bemmerich@yipitdata.com", 'jkelly@yipitdata.com','mrondinaro@yipitdata.com']
message = u'Alternative Data:{}\n\nSatellite Data:{}'.format(alt_data, sat_data)


for recipient in recipients:
    print recipient
    send_me_email.send_html_email(message, recipient, subject)
