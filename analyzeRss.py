import feedparser

feed_urls = ['https://www.vox.com/rss/index.xml'
            , 'https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml'
            ]

#rss = feedparser.parse(feed_urls[0])
#print(rss['feed'].keys())
#feed = rss['feed']
#print(feed['title'])
#for k, v in feed.items():
#    print(k, v)

#print('mult feeds')
feed_data = {}
entry_data = {}
rss_data = {}
for url in feed_urls:
    rss = feedparser.parse(url)
    feed = rss['feed']
    #print('feed keys', feed.keys())
    title = feed['title']
    rss_data[title] = rss
    feed_data[title] = feed

def compare_dicts(n1, d1, n2, d2):
    keys_1 = set(d1.keys())
    keys_2 = set(d2.keys())
    print('shared keys', sorted(keys_1.intersection(keys_2)))
    print('unique to ', n1, sorted(keys_1 - keys_2))
    print('unique to ', n2, sorted(keys_2 - keys_1))
    print()

def compare_sets(n1, s1, n2, s2):
    print('shared keys', sorted(s1.intersection(s2)))
    print('unique to ', n1, sorted(s1 - s2))
    print('unique to ', n2, sorted(s2 - s1))
    print()

def reduce_entry_keys(entries):
    entry_keys = set()
    for e in entries:
        entry_keys.update(e.keys())
    return entry_keys

def optional_entry_keys(n, union_keys, entries):
    optional_keys = set()
    for e in entries:
        optional_keys.update(union_keys - set(e.keys()))
    return optional_keys

print('data feeds')
for name, data_dict in feed_data.items():
    print(name, data_dict)
    for comp_name, comp_data_dict in feed_data.items():
        if name != comp_name:
            print('compare', name, ' to ', comp_name)
            print('rss')
            rss_1 = rss_data[name]
            rss_2 = rss_data[comp_name]
            compare_dicts(name, rss_1, comp_name, rss_2)

            print('feed')
            feed_1 = rss_data[name]['feed']
            feed_2 = rss_data[comp_name]['feed']
            compare_dicts(name, feed_1, comp_name, feed_2)

            print('entries')
            entry_keys_1 = reduce_entry_keys(rss_data[name]['entries'])
            entry_keys_2 = reduce_entry_keys(rss_data[comp_name]['entries'])
            compare_sets(name, entry_keys_1, comp_name, entry_keys_2)
            optional_keys_1 = optional_entry_keys(name, entry_keys_1, rss_data[name]['entries'])
            print(name, ' optional keys ', sorted(optional_keys_1))
            optional_keys_2 = optional_entry_keys(comp_name, entry_keys_2, rss_data[comp_name]['entries'])
            print(comp_name, ' optional keys ', sorted(optional_keys_2))

print('sample data')
for name, data_dict in feed_data.items():
    feed = rss_data[name]['feed']
    print(name, feed['updated'])
    entry = rss_data[name]['entries'][0]
    print(entry['title'], entry['author'], entry['link'])
    print(entry['published'])
    print(entry['published_parsed'])
    #if 'content' in entry:
    #    print(entry['content']['value'])
    print()
