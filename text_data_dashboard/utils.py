from tqdm import tqdm_notebook as tqdm
import pandas as pd
import urllib
import mojimoji

def lower_text(text):
    text=str(text)
    return text.lower()

def lower_zenmoji(df):
    df["text_wakachi"] = df["text_wakachi"].apply(lower_text)
    df["text_wakachi"] = df["text_wakachi"].apply(mojimoji.zen_to_han)
    return df

def get_stopwords():
    req = urllib.request.Request('http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt')
 
    with urllib.request.urlopen(req) as res:
        stopwords = res.read().decode('utf-8').split('\r\n')
    
    while '' in stopwords:
        stopwords.remove('')
    
    return stopwords

def append_list(df):
        
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
        
def extend_list(df):
        
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

def append_listlize(df):
            
    sentences_list = []
    for label in tqdm(range(0, df["label"].nunique())):
                
        df_label = df[df["label"]==label]
        sentences = append_list(df_label)
        sentences_list.append(sentences)
            
    return sentences_list
    
def extend_listlize(df):
            
    sentences_list = []
    for label in tqdm(range(0, df["label"].nunique())):
                
        df_label = df[df["label"]==label]
        sentences = extend_list(df_label)
        sentences_list.append(sentences)
            
    return sentences_list