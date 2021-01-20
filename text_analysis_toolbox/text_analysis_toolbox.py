# -*- coding: utf-8 -*-
import re
import os
import click
import urllib
import logging
import pathlib
import numpy as np
import pandas as pd
import MeCab
from tqdm import tqdm
import mojimoji

import gensim
from dash_app import dash_app_dashboard
from sentiment import get_polarity_dict, wiki_model
from utils import *
from embedding_and_clustering import *
from get_wordcloud import *
from analyzer import mecab_analyzer, dataframe_analyzer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import datasets, manifold, mixture, model_selection
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import FeatureUnion
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class MeanEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = next(iter(self.dim))
        self.dim = 300
    
    def fit(self, X, y):
        return self 
 
    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec] 
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])

class TextAnalysisToolBox:
    
    def __init__(self):
        self.df_wakachi = None
             
    def transform(self, df):
        stopwords = get_stopwords()
        df_separated = dataframe_analyzer(df, stopwords)
        df_parsed = lower_zenmoji(df_separated)
        
        self.df_wakachi = df_parsed
        
        return df_parsed


    def embedding_and_clustering_scatter(self, df, configs):
        
        umap_res, words, labels = embedding_and_clustering(df, configs)
        
        return umap_res, words, labels
    
    def get_vocab(self, df):
        
        return append_list(df)
    
    def lda_wordcloud(self, df):
    
        texts = append_list(df)
    
        dictionary = gensim.corpora.Dictionary(texts)
        dictionary.filter_extremes(no_below=3, no_above=0.8)
        corpus = [dictionary.doc2bow(t) for t in texts]
        
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=8, random_state=0)
        
        get_wordcloud(lda_model)
        
        return lda_model
        
    def create_dashboard(self, df):

        dash_app_dashboard(df)
        
        
        