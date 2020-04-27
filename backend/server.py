from collections import Counter
import random
import tornado.ioloop
import tornado.web
import logging

logging.basicConfig(level=logging.INFO)

class WordCheckHandler(tornado.web.RequestHandler):

    def initialize(self, words_db):
        # TODO а надо ли делать различия между е и ё?
        self.words_db = words_db

    def get(self):
        word = self.get_query_argument('word')
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
        words_counter = Counter([word[:2] for word in words_db])
        self.prefixes_db = [prefix for prefix, _ in words_counter.most_common(50)]

    def get(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.write({'result': random.choice(self.prefixes_db)})

def make_app():
    words_db = set()
    with open('zdf-win.txt') as words:
        for word in words:
            word = word.strip()
            if '-' not in word:
                words_db.add(word)

    return tornado.web.Application([
        (r'/valid', WordCheckHandler, dict(words_db=words_db)),
        (r'/prefix', GetPrefixHandler, dict(words_db=words_db)),
    ])


if __name__ == '__main__':
    logging.info('making app')
    app = make_app()
    app.listen(5050)
    logging.info('serve forever on port 5050')
    tornado.ioloop.IOLoop.current().start()
