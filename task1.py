import stanza
# stanza.download('en')
import urllib3
from bs4 import BeautifulSoup
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

TOLSTOY = "https://www.gutenberg.org/files/985/985-0.txt"
CARROLL = "https://www.gutenberg.org/files/11/11-0.txt"

def get_text(url):
    http = urllib3.PoolManager()
    txt = http.request('GET',url).data
    txt = BeautifulSoup(txt, "html.parser")
    return txt.prettify()

def pos_dict(txt):
    nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
    doc = nlp(txt)
    dict = {"ADJ": 0, "ADP": 0, "ADV": 0, "AUX": 0, "CCONJ": 0, "DET": 0, "INTJ": 0, "NOUN": 0, "NUM": 0, "PART": 0,
            "PRON": 0, "PROPN": 0, "PUNCT": 0, "SCONJ": 0, "SYM": 0, "VERB": 0, "X": 0}
    c = 0
    for sen in doc.sentences:
        for word in sen.words:
            dict[word.upos] += 1
            c += 1
    for key in dict.keys():
        dict[key]/=c
    return dict

dict1 = pos_dict(get_text(TOLSTOY))
dict2 = pos_dict(get_text(CARROLL))

plt.bar(dict1.keys(),dict1.values())
plt.bar(dict2.keys(),dict2.values(),alpha=0.5)

plt.show()