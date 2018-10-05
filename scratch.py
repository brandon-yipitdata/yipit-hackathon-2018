
for d in data:
        row = {
            'run_id' : run_id,
            'uuid': str(uuid.uuid4()),
            'date_story': datetime.datetime.fromtimestamp(int(d['inputtime'])),
            'source' : '21 Jingji',
            'title' : re.sub('<[^<]+?>', '', d['title']),
            'url' : d['url'],
        }

        if row['url'] not in list_of_urls:
            try:
                cur.execute(settings.QUERY_INSERT, row)
                conn.commit()
            except Exception as e:
                print e
                print row['url']
                conn.rollback()
        else:
            print 'We already have this: ' + row['url']
