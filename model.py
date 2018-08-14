from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

Base = declarative_base()


class Feed(Base):
    __tablename__ = 'feed'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)

    entries = relationship("Entry", backref=backref('feed', order_by=id))

    def __repr__(self):
        return "<Feed(title='%s', url='%s')>" % (
            self.title, self.url)


class Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    # contents may be empty (empty string, not null)
    contents = Column(String, nullable=False)
    published = Column(DateTime, nullable=False, index=True)
    summary = Column(String, nullable=False)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    feed_id = Column(Integer, ForeignKey('feed.id'), index=True)

    def __repr__(self):
        return "<Entry(title='%s', url='%s')>" % (
            self.title, self.url)

