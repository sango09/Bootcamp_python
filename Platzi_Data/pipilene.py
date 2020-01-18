import logging
logging.basicConfig(level=logging.INFO)
import subprocess


logger = logging.getLogger(__name__)
news_sites_uids = ['eltiempo','elmundo']


def main():
    _extract()
    _transform()
    _load()


def _extract():
    logger.info('Comenzando extracción de datos')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python3', 'main.py', news_site_uid], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid), 
                        '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid), ';'],
                       cwd='./extract')


def _transform():
    logger.info('Comenzando proceso de transformación')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python3', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)], cwd='./transform')


def _load():
    logger.info('Comenzando proceso de carga')
    for news_site_uid in news_sites_uids:
        clean_data_filename = '{}.csv'.format(news_site_uid)
        subprocess.run(['python3', 'main.py', clean_data_filename], cwd='./load')
    
    logger.info('Proceso finalizado, revisa tu Data Base')

if __name__ == '__main__':
    main()