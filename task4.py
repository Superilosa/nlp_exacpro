import urllib3
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import datamuse

http = urllib3.PoolManager()
txt = http.request('GET',"https://www.gutenberg.org/cache/epub/32415/pg32415.txt").data
txt = BeautifulSoup(txt,'html.parser').prettify()

fstr = ""
cmnt = False
for line in txt.splitlines()[181:9902]:
    if line and line[0].isspace():
        substr = ""
        for c in line[line.find(next(filter(lambda x: x.isalnum() or x == '[' or x == ']', line))):]:
            if c==']':
                cmnt = False
            elif c=='[':
                cmnt = True
            elif not cmnt:
                if c.isalnum() or c.isspace():
                    substr += c
        if substr:
            fstr += substr+'\n'

api = datamuse.Datamuse()
for line in fstr.splitlines():
    wtkn = word_tokenize(line)
    w = wtkn[-1]
    lw = wtkn[-2]
    rh = api.words(rel_rhy=w,lc=lw,max=1)
    print(w,end='\t')
    if len(rh)>0:
        rh = rh[0]["word"]
        print(rh)
    else:
        print()