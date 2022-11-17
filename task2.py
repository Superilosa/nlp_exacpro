from nltk.corpus import wordnet as wn
import fasttext.util
from scipy.spatial.distance import cosine
from scipy.stats import kendalltau

f = open("SimLex-999.txt")
f.readline()
sim = []
line = f.readline()
w1 = []; w2 = []; pos = []
while line:
    line = line.split('\t')
    sim.append(line[3])
    w1.append(line[0])
    w2.append(line[1])
    pos.append(line[2])
    line = f.readline()

# Wordnet synset path similarity
# Fasttext word vectors cosine similarity
wnSim = []
ft = fasttext.load_model(r"C:\Users\iliko\PycharmProjects\project1\venv\Lib\site-packages\fasttext\util\cc.en.300.bin")
ftSim = []
for i in range(len(w1)):
    s1 = wn.synset(w1[i]+'.'+pos[i].lower()+'.01')
    s2 = wn.synset(w2[i]+'.'+pos[i].lower()+'.01')
    wnSim.append(s1.path_similarity(s2))
    v1 = ft.get_word_vector(w1[i])
    v2 = ft.get_word_vector(w2[i])
    ftSim.append(1-cosine(v1,v2))

# Kendall's tau coefficient for similarities
print(kendalltau(sim,wnSim))
print(kendalltau(sim,ftSim))