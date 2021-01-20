from sklearn_pandas import DataFrameMapper
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE
from gensim.models import Word2Vec
import pandas as pd
import numpy as np

def balanced_sampling(X_train, y_train, target_col):
    """Sampling data from imbalanced data
    input: Data Frame, column_names
    output:
    """
    
    smt = SMOTE(random_state=0)
    
    X_resampled, y_resampled = smt.fit_sample(X_train, y_train[target_col])
    
    X_resampled, y_resampled = pd.DataFrame(X_resampled), pd.DataFrame(y_resampled)
    X_resampled.columns, y_resampled.columns = X_train.columns, [target_col]
    
    X_all = pd.concat([y_resampled, X_resampled], axis=1)
    X_all.reset_index(inplace=True); X_all.drop("index", axis=1, inplace=True)
    
    X_train_re, y_train_re = pd.DataFrame(X_all.drop([target_col], axis=1)), pd.DataFrame(X_all[target_col])
    y_train_return.columns = [target_col]
    
    print("Sampled data size is {}".format(X_train_re.shape))
    
    return X_train_re, y_train_re

def build_tfidf(corpus, config):

    df_corpus = corpus[["text_wakachi", "label"]]

    mapper = DataFrameMapper([
        ('text_wakachi', TfidfVectorizer(ngram_range=(2, 2), min_df=5)), 
        (['label'], None)
    ])

    df_mapped = pd.DataFrame(mapper.fit_transform(df_corpus.copy()), columns=mapper.transformed_names_)
    X_mapped, y = df_mapped.drop("label", axis=1), pd.DataFrame(df_mapped["label"].values, columns=["label"])
    
    return X_mapped, y

def build_w2v(df, config):

    word2vecs = Word2Vec(
        sentences = df, iter=config["epoch_num"], size=config["features_num"],
        min_count = config["min_word_count"], window=config["context"], sample=config["downsampling"])

    corpus = [text for text in df["text_wakachi"]]

    avg_w2v = np.array([word2vecs.wv[list(text & word2vecs.wv.vocab.keys())].mean(axis=0) for text in df["text_wakachi"]])
    
    return avg_w2v, df["label"]