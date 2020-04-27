"""
Мой эпичный труд по извлечению слов из википедии
Думал заняться вебскрапингом википедии и попутно приводя предложения в начальную форму собирать
Но нет, психанул и взял словарь Зализняка
Может быть, доработаю идею позже
"""

import requests
import re
import os
import csv
from bs4 import BeautifulSoup
from collections import Counter, deque


def extract_words(html_text):
    result = []
    soup = BeautifulSoup(html_text, 'lxml')
    body = soup.body
    russian_ptrn = re.compile(r'^(?:[А-Я][а-я]+|[а-я]+|[А-Я]+|\(|\))[.,]?$')
    for c in parse_recursively(body):
        for word in re.split(r'[^\w.,]+', c):
            if russian_ptrn.match(word):
                result.append(word)
    return ' '.join(result)


def parse_recursively(tag):
    result = []
    for c in tag.contents:
        d = 0
        try:
            for a in c.children:
                if a.name:
                    d += 1
                    result += parse_recursively(a)
            if not d:
                result.append(c.text)
        except Exception as e:
            result.append(c)
    return result


def extract_links(html_text):
    result = set()
    soup = BeautifulSoup(html_text, 'lxml')
    def rel_ref(href):
        return href and (href.startswith('/w') or href.startswith('//ru.wikipedia.org'))
    for tag in soup.find_all(href=rel_ref):
        if tag['href'].startswith('//ru.wikipedia.org'):
            result.add(tag['href'][:18])  # len('//ru.wikipedia.org')
        else:
            result.add(tag['href'])
    return result


def save_all_words_on_page_and_return_internal_links(url, fname):
    response = requests.get('https://ru.wikipedia.org' + url)
    if response.status_code == 200:
        links = extract_links(response.text)
        counter = Counter([word.lower() for word in extract_words(response.text)])
        with open(os.path.join('words', fname), 'w', newline='\n', encoding='utf-8') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerows(counter.most_common())
        return links


def main():
    links_visited_count = 0
    links_visited = set()
    links_queue = deque(['/'])
    while links_visited_count < 2 or links_queue:
        link = links_queue.popleft()
        if link not in links_visited:
            links_queue += save_all_words_on_page_and_return_internal_links(link, str(links_visited_count + 1) + '.csv')
            links_visited.add(link)
            links_visited_count += 1


# import rutokenizer
# import rupostagger
# import rulemma
#
# lemmatizer = rulemma.Lemmatizer()
# lemmatizer.load()
#
# tokenizer = rutokenizer.Tokenizer()
# tokenizer.load()
#
# tagger = rupostagger.RuPosTagger()
# tagger.load()

response = requests.get('https://ru.wikipedia.org/')
if response.status_code == 200:
    # print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    for tag in soup.select('style, script, link, meta'):
        tag.extract()
            #print(tag.prettify())
    print(soup.prettify())
    # print(extract_words(response.text))
    # sent = u'Мяукая, голодные кошки ловят жирненьких хрюнделей'
    #sent = extract_words(response.text)
    # tokens = tokenizer.tokenize(sent)
    # tags = tagger.tag(tokens)
    # lemmas = lemmatizer.lemmatize(tags)
    # for word, tags, lemma, *_ in lemmas:
    #     print(u'{:15}\t{:15}\t{}'.format(word, lemma, tags))
