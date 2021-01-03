# -*- coding: utf-8 -*-
import re
import os
import click
import urllib
import logging
from pathlib import Path
import numpy as np
import pandas as pd
import MeCab
from tqdm import tqdm
import mojimoji
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

class TextDataDashboard:
    
    def __init__(self):
        pass
    
    def _get_stopwords(self):
        req = urllib.request.Request('http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt')
 
        with urllib.request.urlopen(req) as res:
            stopwords = res.read().decode('utf-8').split('\r\n')
    
        while '' in stopwords:
            stopwords.remove('')
    
        return stopwords
    
    def _tokenizer(self, text, stopwords):
        tagger = MeCab.Tagger("mecabrc")
        tagger.parse('')
        node = tagger.parseToNode(text)
        keywords = []
  
        while node:
            meta = node.feature.split(",") 
            if meta[0] == "名詞" or meta[0] == "形容詞":
                if meta[6] != "*":
                    if meta[6] not in stopwords:
                        keywords.append(meta[6])
                else:
                    pass
            node = node.next
        return keywords

    def _word_separator(self, df, stopwords):
        wakachi_list = []
        wakachi_total_list = []
        for i, di in tqdm(enumerate(df['text'])):
            w = self._tokenizer(di, stopwords)
            wakachi_list = ' '.join(w)
            #while '' in stopwords:
            #    wakachi_list.remove('')
            wakachi_total_list += [wakachi_list]
        # merge data
        wakachi_data = pd.DataFrame(wakachi_total_list)
        wakachi_data.columns=["text_wakachi"]
        new_wakachi = pd.concat([df, wakachi_data], axis=1)
        
        return new_wakachi
    
    def _lower_text(self, text):
        text=str(text)
        return text.lower()

    def _lower_zenmoji(self, df):
        df["text_wakachi"] = df["text_wakachi"].apply(self._lower_text)
        df["text_wakachi"] = df["text_wakachi"].apply(mojimoji.zen_to_han)
        return df
    
    def transform(self, df):
        stopwords = self._get_stopwords()
        df_separated = self._word_separator(df, stopwords)
        df_parsed = self._lower_zenmoji(df_separated)
        
        return df_parsed
    
    def create_dashboard(df):
        
        # config
        PATH = pathlib.Path(__file__).parent
        DATA_PATH = PATH.joinpath("data").resolve()

        app = dash.Dash(
            __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
        )
        server = app.server


        # Create global chart template
        mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
