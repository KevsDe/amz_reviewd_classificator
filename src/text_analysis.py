import pandas as pd
from textblob import TextBlob
def sentimental(review):
    classifier = TextBlob
    polarity = []
    subjectivity = []
    for idx in range(len(review)):
        polarity.append(classifier(review[idx]).sentiment[0])
        subjectivity.append(classifier(review[idx]).sentiment[1])
    polarity = [round(num,2) for num in polarity ]
    subjectivity = [round(num, 2) for num in subjectivity]
    return (polarity, subjectivity)

import textstat
def textscore(review):
    lexicon_count = []
    flesch_reading = []
    for idx in range(len(review)):
        lexicon_count.append(textstat.lexicon_count(review[idx], removepunct=True))
        flesch_reading.append(textstat.flesch_reading_ease(review[idx]))
    return (lexicon_count,flesch_reading)



import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter


def tag_counter(tag, review):
    tg = {'verbs': ['VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
          'nouns': ['NN', 'NNS', 'NNP', 'NNPS'],
          'prp': ['PRP']
          }

    tag = tg[tag]

    text = nltk.word_tokenize(review)
    tags = nltk.pos_tag(text)
    counts = Counter(tag for word, tag in tags)
    tag_lst = []
    for idx in counts.keys():
        if idx in tag:
            tag_lst.append(idx)
    num_tags = 0
    for idx in tag_lst:
        num_tags += counts[idx]
    return num_tags


def tags_collector(tag, review):
    lst = []
    for idx in range(len(review)):
        lst.append(tag_counter(tag, review[idx]))
    return lst


def ratio(data,column,category):
    """Calculate ratios based in three parameters data frame, column and the attribute of the column, the columna and categoria parameters should be a string"""
    a=data[data[column]==category]
    b=data[column]

    p1=len(a)
    p2=len(b)
    ratio=(p1/p2)*100
    return ratio


from nltk.tokenize import word_tokenize


def nltk_tokenizer(sentence):
    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = word_tokenize(sentence)

    # return preprocessed list of tokens
    return mytokens