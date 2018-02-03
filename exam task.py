#5 баллов: написать программу, которая автоматически обращалась бы к странице http://web-corpora.net/Test2_2016/short_story.html,
#доставала оттуда все слова, начинающиеся на кириллическую букву «с». Слова нужно распечатать на экране в столбик.

#8 баллов: с помощью Mystem найти для этих слов части речи, выделить среди них глаголы и распечатать на экране в столбик.

import urllib.request
import re

def browsing():
    req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(req) as a:
        html = a.read().decode('utf-8')
        with open('swordlst.txt', 'a', encoding='utf-8') as swordlist:
            swordlist.write(html)

def swordfight():
    swords = re.compile('[^а-яА-Я](С|с[а-яА-Я]{0,})')
    with open('swordlst.txt', 'r', encoding='utf-8') as swordlist:
        sabers = swordlist.read()
        sgswords = re.findall(swords, sabers)
        arrows = []
        for i in range((len(sgswords))):
            if sgswords[i] not in arrows:
                arrows.append(sgswords[i])
        print('\n'.join(arrows))
        
browsing()
swordfight()
