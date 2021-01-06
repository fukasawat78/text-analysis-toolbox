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

def mecab_analyzer(text, stopwords):
    tagger = MeCab.Tagger("mecabrc")
    tagger.parse('')
    node = tagger.parseToNode(text)
    keywords = []
  
    while node:
        meta = node.feature.split(",") 
        if meta[0] == "名詞":
            if meta[6] != "*":
                if meta[6] not in stopwords:
                    keywords.append(meta[6])
            else:
                pass
        node = node.next
    return keywords

def dataframe_analyzer(df, stopwords):
    
    wakachi_list = []
    wakachi_total_list = []
    for i, di in tqdm(enumerate(df['text'])):
        w = mecab_analyzer(di, stopwords)
        wakachi_list = ' '.join(w)
        #while '' in stopwords:
        #    wakachi_list.remove('')
        wakachi_total_list += [wakachi_list]
    # merge data
    wakachi_data = pd.DataFrame(wakachi_total_list)
    wakachi_data.columns=["text_wakachi"]
    new_wakachi = pd.concat([df, wakachi_data], axis=1)
        
    return new_wakachi

def janome_analyzer(df, label=0):
    news_df = df[df["label"] == label].reset_index(drop = True)

    t = Tokenizer()
    char_filters = UnicodeNormalizeCharFilter()
    analyzer = Analyzer()

    word_lists = []
    for i, row in news_df.iterrows():    
        for t in analyzer.analyze(row["text"]):
            #形態素
            surf = t.surface
            #基本形
            base = t.base_form
            #品詞
            pos = t.part_of_speech
            #読み
            reading = t.reading

            word_lists.append([i, surf, base, pos, reading])

    word_df = pd.DataFrame(word_lists, columns = ['ニュースNo.', '単語', '基本形', '品詞', '読み'])
    word_df['品詞'] = word_df['品詞'].apply(lambda x : x.split(',')[0])
    
    return word_df