import nltk
import re
import spacy
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
#
from .Models import *


class Simple(object):
    def __init__(self, text):
        self.text = re.sub(r"\W+", " ", text).lower()
        self.tokens = word_tokenize(self.text)
        self.stemmer = SnowballStemmer("spanish")
        self.lemmatizer = WordNetLemmatizer()
        self.dependency_parser = spacy.load('es_core_news_sm')
        self.parsed_text = self.dependency_parser(self.text)
        self.bag = BagOfWords(self.tokens)

    def stem(self):
        return [self.stemmer.stem(token) for token in self.tokens]

    def lemmatize(self):
        return [self.lemmatizer.lemmatize(token) for token in self.tokens]

    def tree(self, node):
        if node.n_lefts + node.n_rights > 0:
            parsed_child_nodes = [self.tree(child) for child in node.children]
            return nltk.Tree(node.orth_, parsed_child_nodes)
        else:
            return node.orth_

    def show_tree(self):
        for sent in self.parsed_text.sents:
            return self.tree(sent.root)
