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
            if meta[0] == "名詞":
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
    
    def _append_list(self, df):
        
        sentences=[]

        for review in tqdm(df["text_wakachi"]):
            try:
                result = review.replace("\u3000", "").replace("\n","")
                #result = re.sub(r'[0123456789０１２３４５６７８９！＠＃＄％＾＆\-|\\＊\*"（）+=){}:;,!.]', "", result)        
                h = result.split(" ")
                h = list(filter(("").__ne__,h))
                sentences.append(h)

            except:
                pass
            
        return sentences
        
    def _extend_list(self, df):
        
        sentences=[]

        for review in tqdm(df["text_wakachi"]):
            try:
                result = review.replace("\u3000", "").replace("\n","")
                #result = re.sub(r'[0123456789０１２３４５６７８９！＠＃＄％＾＆\-|\\＊\*"（）+=){}:;,!.]', "", result)        
                h = result.split(" ")
                h = list(filter(("").__ne__,h))
                sentences.extend(h)

            except:
                pass
            
        return sentences
            
    def _append_listlize(self, df):
            
        sentences_list = []
        for label in tqdm(range(0, df["label"].nunique())):
                
            df_label = df[df["label"]==label]
            sentences = self._append_list(df_label)
            sentences_list.append(sentences)
            
        return sentences_list
    
    def _extend_listlize(self, df):
            
        sentences_list = []
        for label in tqdm(range(0, df["label"].nunique())):
                
            df_label = df[df["label"]==label]
            sentences = self._extend_list(df_label)
            sentences_list.append(sentences)
            
        return sentences_list
                
    def transform(self, df):
        stopwords = self._get_stopwords()
        df_separated = self._word_separator(df, stopwords)
        df_parsed = self._lower_zenmoji(df_separated)
        
        return df_parsed
    
    def create_dashboard(self, df):
        
        # config
        PATH = pathlib.Path(__file__).parent
        DATA_PATH = PATH.joinpath("data").resolve()

        app = dash.Dash(
            __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
        )
        server = app.server


        # Create global chart template
        mapbox_access_token = "pk.eyJ1IjoicGxvdGx5bWFwYm94IiwiYSI6ImNrOWJqb2F4djBnMjEzbG50amg0dnJieG4ifQ.Zme1-Uzoi75IaFbieBDl3A"
        
        from collections import Counter 
        
        sentences_list =  self._extend_listlize(df)
        letter_counts = Counter(sentences_list[0]) 
        df = pd.DataFrame.from_dict(letter_counts, orient='index') 
        df.columns = ["単語頻度"]
        df_sort = df["単語頻度"][:100].sort_values(ascending=False)
        
        histg = go.Figure()

        histg.add_trace(
            go.Scatter(
                x=df_sort.index, y=df_sort,
                name="単語出現頻度",
            )
        )

        app.layout = html.Div(
            [
                html.Div(
                    [
                        html.H2('ダッシュボード',
                                style={'display': 'inline',
                                       'float': 'left',
                                       'font-size': '2.65em',
                                       'margin-left': '7px',
                                       'font-weight': 'bolder',
                                       'font-family': 'Product Sans',
                                       'color': "rgba(117, 117, 117, 0.95)",
                                       'margin-top': '20px',
                                       'margin-bottom': '0'
                                       }),
                        html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe.png",
                                 style={
                                     'height': '100px',
                                     'float': 'right'
                                     },
                                 ),
                        ]
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(
                                            [
                                                dcc.Graph(
                                                    id="",
                                                    figure=histg
                                                ),
                                            ], style={'background-color': '#ffffff', 'text-align': 'center', 'border-radius': '5px 0px 0px 5px', 'height': '700px',
                                              'margin': '10px 0px 10px 10px', 'padding': '15px', 'position': 'relative', 'box-shadow': '4px 4px 4px lightgrey',
                                                    }

                                        ),
                                    ],
                                    id="",
                                    className="row container-display",
                                ),
                            ],
                            id="",
                            className="",
                        ),

                    ],
                    className="row flex-display",
                ),
            ],
            id="mainContainerhoge",
            style={"display": "flex", "flex-direction": "column"},
        )
        
        app.run_server(debug=True)