# -*- coding: utf-8 -*-
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import pandas as pd
import smtplib
import twitter


def get_twitter_data(keyword, count):
    """This function takes a keyword and returns N tweets matching that keyword"""
    print keyword
    empty_list = []

    results = api.GetSearch(
        raw_query="q={}%20&result_type=recent&since=2018-01-01&count={}".format(keyword, str(count)))

    for i in range(len(results)):
        _dict = {
            'Keyword' : keyword.replace("Alternative Data","").strip(),
            'Text' : results[i].text,
            'Link': 'https://twitter.com/statuses/'+str(results[i].id),
        }

        empty_list.append(_dict)

    df = pd.DataFrame(empty_list)
    df = df[df['Text'].str.startswith('RT') == False] # Remove retweets, text always begins with 'RT'
    df['Text'] = df['Text'].str.replace("https://.*",'') # Remove tinyurls
    df = df.drop_duplicates(['Text'],keep = 'first')

    return df



def send_html_email(html, recipient, subject):
	"""This function sends an HTML email from my personal email"""

	fromaddress = private.EMAIL_FROM_ADDRESS

	message = MIMEMultipart("alternative", None, [MIMEText(html,'html','utf-8')])
	message['From'] = fromaddress
	message['Subject'] = subject

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddress, private.EMAIL_PASSWORD)
	text = message.as_string()
	server.sendmail(fromaddress, recipient, text)
	server.quit()
