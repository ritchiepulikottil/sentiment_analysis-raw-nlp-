import string
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


txt = open("ritch.txt", encoding="utf-8").read()
lcase = txt.lower()
clean = lcase.translate(str.maketrans("","",string.punctuation))
seperate = word_tokenize(clean, "english")


req = []
for i in seperate:
    if i not in stopwords.words("english"):
        req.append(i)
        

emolist = []
fh = open("emotions.txt")
for line in fh:
    strip = line.strip().replace("'","").replace(",", "")
    m,n = strip.split(":")
    
    if m in req :
        emolist.append(n)

w = Counter(emolist)
print(w)
fig, ax1 = plt.subplots()
def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score["neg"]
    pos = score["pos"]
    if neg>pos:
        fig.suptitle('OVERALL RESULT : NEGATIVE SENTIMENT', fontsize=14, fontweight='bold')
    elif pos>neg:
        fig.suptitle('OVERALL RESULT : POSITIVE SENTIMENT', fontsize=14, fontweight='bold')
    else:
        fig.suptitle('OVERALL RESULT : NEUTRAL SENTIMENT', fontsize=14, fontweight='bold')
sentiment_analyze(clean)



ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

plt.savefig("result.png")
plt.show()





