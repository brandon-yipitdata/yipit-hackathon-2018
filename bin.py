import pandas as pd
import send_me_email
import twitter_data

insights = twitter_data.get_twitter_data(keyword = 'Alternative Data insights', count = 50).to_html(index = False)
capital = twitter_data.get_twitter_data(keyword = 'Alternative data capital', count = 50).to_html(index = False)
financial = twitter_data.get_twitter_data(keyword = 'Alternative data financial', count = 50).to_html(index = False)
research = twitter_data.get_twitter_data(keyword = 'Alternative data research', count = 50).to_html(index = False)
china = twitter_data.get_twitter_data(keyword = 'Alternative data china', count = 50).to_html(index = False)
careers = twitter_data.get_twitter_data(keyword = 'Alternative data careers', count = 50).to_html(index = False)
company = twitter_data.get_twitter_data(keyword = 'Alternative data company', count = 50).to_html(index = False)
services = twitter_data.get_twitter_data(keyword = 'Alternative data services', count = 50).to_html(index = False)
datasets = twitter_data.get_twitter_data(keyword = 'Alternative data datasets', count = 50).to_html(index = False)


subject = "Alt Data Sourcing Bot"
recipients = ["bemmerich@yipitdata.com", 'jkelly@yipitdata.com','mrondinaro@yipitdata.com']
message = u'Insights:{}\n\nCapital:{}\n\nFinancial:{}\n\nresearch:{}\n\nChina:{}\n\nCareers:{}\n\nCompany:{}\n\nServices:{}\n\nDatasets:{}'.format(insights, capital, financial, research, china, careers, company, services, datasets)


for recipient in recipients:
    print recipient
    send_me_email.send_html_email(message, recipient, subject)
