import model
import config
import feedparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.connection_string, echo=True)
model.Base.metadata.drop_all(engine)
model.Base.metadata.create_all(engine)

#model.Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

feed_urls = ['https://www.vox.com/rss/index.xml'
            , 'https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml'
            ]
try:
    for url in sorted(feed_urls):
        rss = feedparser.parse(url)
        feed_dict = rss['feed']
        title = feed_dict['title']
        feed = model.Feed(title=title, url=url)
        session.add(feed)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
