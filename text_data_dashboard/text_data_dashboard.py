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
from dash_app import dash_app_dashboard
from sentiment import get_polarity_dict, wiki_model
from utils import *
from analyzer import mecab_analyzer, dataframe_analyzer
import jaconv
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *

class TextDataDashboard:
    
    def __init__(self):
        self.df_wakachi = None
             
    def transform(self, df):
        stopwords = get_stopwords()
        df_separated = dataframe_analyzer(df, stopwords)
        df_parsed = lower_zenmoji(df_separated)
        
        self.df_wakachi = df_parsed
        
        return df_parsed
    
    def create_dashboard(self, df):

        dash_app_dashboard(df)
        
        
        