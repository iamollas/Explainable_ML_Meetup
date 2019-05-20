import re
import string

from bs4 import BeautifulSoup
from nltk import WordPunctTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

class MyTextPreproccesor:
    def clean(text):
        tok = WordPunctTokenizer()
        pat1 = '@[\w\-]+'  # for @
        pat2 = ('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|'
                '[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # for url
        pat3 = '#[\w\-]+'  # for hashtag
        pat4 = 'ï»¿'
        pat5 = '[' + string.punctuation + ']'  # for punctuation
        pat6 = '[^\x00-\x7f]'
        soup = BeautifulSoup(text, 'html.parser')  # html decoding ("@amp")
        souped = soup.get_text()
        souped = re.sub(pat1, '', souped)  # remove @
        souped = re.sub(pat2, '', souped)  # remove url
        souped = re.sub(pat4, '', souped)  # remove strange symbols
        souped = re.sub(pat5, '', souped)  # remove punctuation
        souped = re.sub(pat3, '', souped)  # remove "#" symbol and keeps the words
        clean = re.sub(pat6, '', souped)  # remove non-ascii characters
        lower_case = clean.lower()  # convert to lowercase
        words = tok.tokenize(lower_case)
        return (" ".join(words)).strip()
    def my_clean(text,stops = False,stemming = False,minLength = 2):
        text = text.lower().split()
        text = [w for w in text if len(w) >= minLength]
        if stemming and stops:
            text = [word for word in text if word not in stopwords.words('english')]
            wordnet_lemmatizer = WordNetLemmatizer()
            englishStemmer = SnowballStemmer("english", ignore_stopwords=True)
            text = [englishStemmer.stem(word) for word in text]
            text = [wordnet_lemmatizer.lemmatize(word) for word in text]
            #text = [lancaster.stem(word) for word in text]
            text = [word for word in text if word not in stopwords.words('english')]
        elif stops:
            text = [word for word in text if word not in stopwords.words('english')]
        elif stemming:
            wordnet_lemmatizer = WordNetLemmatizer()()
            englishStemmer = SnowballStemmer("english", ignore_stopwords=True)
            text = [englishStemmer.stem(word) for word in text]
            text = [wordnet_lemmatizer.lemmatize(word) for word in text]
        text = " ".join(text)
        text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub(r",", " ", text)
        text = re.sub(r"\.", " ", text)
        text = re.sub(r"!", " ! ", text)
        text = re.sub(r"\/", " ", text)
        text = re.sub(r"\^", " ^ ", text)
        text = re.sub(r"\+", " + ", text)
        text = re.sub(r"\-", " - ", text)
        text = re.sub(r"\=", " = ", text)
        text = re.sub(r"'", " ", text)
        text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
        text = re.sub(r":", " : ", text)
        text = re.sub(r" e g ", " eg ", text)
        text = re.sub(r" b g ", " bg ", text)
        text = re.sub(r" u s ", " american ", text)
        text = re.sub(r"\0s", "0", text)
        text = re.sub(r" 9 11 ", "911", text)
        text = re.sub(r"e - mail", "email", text)
        text = re.sub(r"j k", "jk", text)
        text = re.sub(r"\s{2,}", " ", text)
        text = text.lower().split()
        text = [w for w in text if len(w) >= minLength]
        if stemming and stops:
            text = [word for word in text if word not in stopwords.words('english')]
            wordnet_lemmatizer = WordNetLemmatizer()
            englishStemmer = SnowballStemmer("english", ignore_stopwords=True)
            text = [englishStemmer.stem(word) for word in text]
            text = [wordnet_lemmatizer.lemmatize(word) for word in text]
            # text = [lancaster.stem(word) for word in text]
            text = [word for word in text if word not in stopwords.words('english')]
        elif stops:
            text = [word for word in text if word not in stopwords.words('english')]
        elif stemming:
            wordnet_lemmatizer = WordNetLemmatizer()()
            englishStemmer = SnowballStemmer("english", ignore_stopwords=True)
            text = [englishStemmer.stem(word) for word in text]
            text = [wordnet_lemmatizer.lemmatize(word) for word in text]
        text = " ".join(text)
        return text

