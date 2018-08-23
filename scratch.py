import pandas as pd
import send_me_email
import twitter


api = twitter.Api(consumer_key='LhW03ocGwIrKqKl1ahZsVojGV',
    consumer_secret='QGB5h51326GF2IEeRy2b0jhHgyQwRhpMJAnJeFOaiglEAwnIZn',
    access_token_key='822878689222422532-wyK39KUvM6eLQkbURVgB5Gq6JVMJwz0',
    access_token_secret='qCrN9eV0h8YHYys9Qu0g3dmN4iFYLVLTmAKUJ76dFoyOi')


keyword = "Alt Data"
count = 100

results = api.GetSearch(
    raw_query="q={}%20&result_type=recent&since=2018-01-01&count={}".format(keyword, str(count)))


empty_list = []

for i in range(len(results)):
    _dict = {
        'text' : results[i].text,
    }

    empty_list.append(_dict)

df = pd.DataFrame(empty_list)
#df['date_time'] = pd.to_datetime(df.date_time)
pd.set_option('display.max_colwidth', 90)

import ipdb; ipdb.set_trace()

subject = "Hackathon"
recipient = "bemmerich@yipitdata.com"
message = u'This is your data:{}'.format(df.to_html(index = False))


send_me_email.send_html_email(message, recipient, subject)
