import nltk
import urllib2
from bs4 import BeautifulSoup
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

#SOTU speeches available at:
#http://stateoftheunion.onetwothree.net/texts/

#Takes a list of words, remove common ones
def remove_stop_words(tokens):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in tokens if w.lower() not in stopwords]
    return content

#Takes a list of words, lowercases them
def lowercase_tokens(tokens):
    list_of_words = []
    for a in tokens:
        a = a.lower()
        list_of_words.append(a)
    return list_of_words

def remove_common_SOTU_words(tokens):
    SOTU_words = ["united", "states", "america", "congress",
                  "senate", "federal", "government", "state"]
    content = [w for w in tokens if w.lower() not in SOTU_words]
    return content

#Load speech from web, extract text
SOTU = "http://stateoftheunion.onetwothree.net/texts/17971122.html"
html = urllib2.urlopen(SOTU).read().decode('utf8')
text = BeautifulSoup(html).get_text()

#Create tokenizer to remove punctuation and numbers
tokenizer = RegexpTokenizer(r'\w+')

#Tokenize, lowercase, remove stop words
tokens = tokenizer.tokenize(text)
tokens = lowercase_tokens(tokens)
tokens = remove_stop_words(tokens)
tokens = remove_common_SOTU_words(tokens)
fdist = FreqDist(tokens)

#Print common words
print fdist.most_common(10)
