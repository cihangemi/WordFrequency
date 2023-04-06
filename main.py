import operator
import requests
from bs4 import BeautifulSoup
from clrsymbol import clearSymbols
from clrnums import clearNums
from createDict import wordCounter

url = "https://tr.wikipedia.org/wiki/Osmanlı_İmparatorluğu"
allwords=[]
r = requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")

for wordgrups in soup.find_all("p"):
    content = wordgrups.text
    words = content.lower().split()

    for word in words:
        allwords.append(word)


allwords0 = clearSymbols(allwords)
allwords1 = clearNums(allwords0)
word_count = wordCounter(allwords1)

for anahtar,deger in sorted(word_count.items(),key = operator.itemgetter(1)):
    print(anahtar,deger)