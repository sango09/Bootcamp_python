from sqlalchemy import Column, String, Integer

from base import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    tokens_counter_body = Column(Integer)
    tokens_counter_title = Column(Integer)
    url = Column(String, unique=True)

    def __init__(self,
                 uid,
                 body,
                 host,
                 newspaper_uid,
                 tokens_counter_body,
                 tokens_counter_title,
                 title,
                 url):
        self.id = uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.tokens_counter_body = tokens_counter_body
        self.tokens_counter_title = tokens_counter_title
        self.title = title
        self.url = url
