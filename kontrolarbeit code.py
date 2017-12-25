# Извлечь с каждой страницы пары "тайское слово -- английское слово" и поместить их в словарь,
#где ключом будет тайское слово, а значением - английское.

# Записать её в файл формата json на диск, а также создать ещё одну структуру данных, где будет наоборот:
# английское слово ключ, а массив тайских слов - значение. Её тоже записать на диск в формате json.


import re
import os
#import json

#здесь, наверное, нужно пояснить, что происходит, потому что в коде itself я очень сильно не уверена
#читаю файл (теоретически, нужно прочесть все файлы в папке, но я не помню, как это делается);
#вытаскиваю из него массивы тайских и английских слов, чистя от тэгов; свожу их в словарь; радуюсь жизни (нет)

def reading():
    ## притворяемся браузером
    with open('187.31.html', 'r', encoding='utf-8') as a:
        article = a.read()
        a.close()

def thaiwords():
    regthaiwords = re.compile('<td class="th">.*?</td>', flags= re.DOTALL)
    thaiwords = regthaiwords.findall(html)
    purethai = []
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    for a in purethai:
        clean_a = regSpace.sub("", a)
        clean_a = regTag.sub("", clean_a)
        purethai.append(clean_a)

def engwords():
    regengwords = re.compile('<td>.*?</td>', flags= re.DOTALL)
    engwords = regthaiwords.findall(html)
    pureeng = []
    regTag = re.compile('<.*?>', re.DOTALL)
    regSpace = re.compile('\s{2,}', re.DOTALL)
    for b in pureeng:
        clean_b = regSpace.sub("", b)
        clean_b = regTag.sub("", clean_b)
        pureeng.append(clean_b)

def dictionary(thaiwords, engwords):
    thaieng = dict([purethai, pureeng])
