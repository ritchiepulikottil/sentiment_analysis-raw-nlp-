import string
from collections import Counter
import matplotlib.pyplot as plt
txt = open("ritch.txt", encoding="utf-8").read()
lcase = txt.lower()
clean = lcase.translate(str.maketrans("","",string.punctuation))
seperate = clean.split()

#here the stop words are defined manually, hence less efficient
#use NLTK package instead which is predefined with better stop words
stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself","yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself","they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these","those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do","does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while","of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before","after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again","further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each","few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than","too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


req = []
for i in seperate:
    if i not in stopword:
        req.append(i)
#better emotions.txt available @NLTK
emolist = []
fh = open("emotions.txt")
for line in fh:
    strip = line.strip().replace("'","").replace(",", "")
    m,n = strip.split(":")
    
    if m in req :
        emolist.append(n)

w = Counter(emolist)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

plt.savefig("result.png")
plt.show()





