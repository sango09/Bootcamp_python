from base import Base, engine, Session
from article import Article
import pandas as pd
import argparse
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(filename):
    Base.metadata.create_all(engine)
    session = Session()
    articles = pd.read_csv(filename)

    for index, row in articles.iterrows():
        logger.info(
            'Cargando articulos uid {} dentro de la Data Base'.format(row['uid']))
        article = Article(row['uid'],
                          row['body'],
                          row['host'],
                          row['newspaper_uid'],
                          row['tokens_counter_body'],
                          row['tokens_counter_title'],
                          row['title'],
                          row['url'])
        session.add(article)

    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='El archivo que quieres cargar a la Data Base',
                        type=str)

    args = parser.parse_args()

    main(args.filename)
