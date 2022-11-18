import pandas as pd
import stanza
from sklearn.metrics import accuracy_score

txt = pd.read_csv("yelp_labelled.txt",sep='\t',names=["sentence","p"],dtype=str)
sWords = pd.read_csv("SentiWords_1.1.txt",sep='\t',skiprows=26,names=["lemma","prior_polarity_scores"])
nlp = stanza.Pipeline('en',processors='tokenize,pos,lemma,sentiment',tokenize_no_ssplit=True)
posConv = {"NOUN":"n","VERB":"v","ADJ":"a","ADV":"r"}
s_scores = []
stanza_scores = []
for sentence in txt["sentence"].values:
    doc = nlp(sentence)
    sp = 0
    for sen in doc.sentences:
        stanza_scores.append(sen.sentiment)
        wNot = False
        for word in sen.words:
            lem = word.lemma
            pos = word.upos
            if pos in posConv:
                p = sWords[sWords["lemma"]==lem.lower()+"#"+posConv[pos]]["prior_polarity_scores"].values
                if len(p)==1:
                    if wNot:
                        p[0] *= -1
                    sp += p[0]
            if lem == "not":
                wNot=True
            else:
                wNot=False
    if sp > 0:
        s_scores.append(1)
    else:
        s_scores.append(0)

print(accuracy_score(txt["p"].astype(int),s_scores))
print(len(txt["p"].values),len(s_scores),len(stanza_scores))