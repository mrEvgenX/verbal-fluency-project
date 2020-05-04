from collections import Counter
import random
import tornado.ioloop
import tornado.web
import logging

logging.basicConfig(level=logging.INFO)


class WordCheckHandler(tornado.web.RequestHandler):

    def initialize(self, words_db):
        self.words_db = words_db

    def get(self):
        word = self.get_query_argument('word').strip().replace('ё', 'е')
        logging.info('validation called with %s', word)
        self.set_header('Access-Control-Allow-Origin', '*')
        if word in self.words_db:
            self.write({'result': True})
        else:
            self.write({'result': False})


class GetPrefixHandler(tornado.web.RequestHandler):

    def initialize(self, words_db):
        # TODO от частоты настраивать уровень сложности
        logging.info('prefix generation called')
        prefix_length = int(self.get_query_argument('prefix_length').strip())
        words_counter = Counter([word[:prefix_length] for word in words_db])
        self.prefixes_db = [prefix for prefix, _ in words_counter.most_common(50)]

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write({'result': random.choice(self.prefixes_db)})


class WordHinterHandler(tornado.web.RequestHandler):

    def initialize(self, words_db):
        self.words_db = words_db

    def get(self):
        prefix = self.get_query_argument('prefix')
        words = [word.strip().replace('ё', 'е') for word in self.get_query_arguments('word[]')]
        # print(len([word for word in self.words_db if word.startswith(prefix) and word not in words]))
        words_counter = Counter([word for word in self.words_db if word.startswith(prefix) and word not in words])
        for i in words_counter:
            print(i)
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write({'result': []})


def make_app():
    words_db = set()
    with open('zdf-win.txt') as words:
        for word in words:
            word = word.strip().replace('ё', 'е')
            if '-' not in word:
                words_db.add(word)

    return tornado.web.Application([
        (r'/valid', WordCheckHandler, dict(words_db=words_db)),
        (r'/prefix', GetPrefixHandler, dict(words_db=words_db)),
        (r'/hint', WordHinterHandler, dict(words_db=words_db)),
    ])


if __name__ == '__main__':
    logging.info('making app')
    app = make_app()
    app.listen(5050)
    logging.info('serve forever on port 5050')
    tornado.ioloop.IOLoop.current().start()
