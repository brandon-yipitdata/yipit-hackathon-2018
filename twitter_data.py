import pandas as pd
import twitter

pd.set_option('max_colwidth', 280)

api = twitter.Api(consumer_key='LhW03ocGwIrKqKl1ahZsVojGV',
    consumer_secret='QGB5h51326GF2IEeRy2b0jhHgyQwRhpMJAnJeFOaiglEAwnIZn',
    access_token_key='822878689222422532-wyK39KUvM6eLQkbURVgB5Gq6JVMJwz0',
    access_token_secret='qCrN9eV0h8YHYys9Qu0g3dmN4iFYLVLTmAKUJ76dFoyOi')

def get_twitter_data(keyword, count):
    """This function takes a keyword and returns N tweets matching that keyword"""

    results = api.GetSearch(
        raw_query="q={}%20&result_type=recent&since=2018-01-01&count={}".format(keyword, str(count)))

    empty_list = []

    for i in range(len(results)):
        _dict = {
            'text' : results[i].text,
            'link': 'https://twitter.com/statuses/'+str(results[i].id),
        }

        empty_list.append(_dict)

    df = pd.DataFrame(empty_list)

    return df
