import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from utils import *
from gensim.models import Word2Vec
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import umap.umap_ as umap
import hdbscan

def get_word2vec(df):
    # Parameter
    features_num = 300
    min_word_count=10
    context=5
    downsampling = 1e-3
    epoch_num=10

    corpus = append_list(df)

    word2vec_model = Word2Vec(
        sentences = corpus, iter=epoch_num, size=features_num,
        min_count=min_word_count, window=context, sample=downsampling,
    )
    
    vocab = word2vec_model.wv.vocab
    emb_tuple = tuple([word2vec_model[v] for v in vocab])
    X = np.vstack(emb_tuple)
    
    return X, vocab, word2vec_model

def get_umap(X, configs):
    
    umap_res = umap.UMAP(
        n_neighbors=configs["n_neighbors"], 
        n_components=configs["n_components"]
    ).fit_transform(X)
    
    return umap_res

def get_hdbscan(X, configs):
    
    labels = hdbscan.HDBSCAN(
        min_samples=configs["min_samples"],
        min_cluster_size=configs["min_cluster_size"],
    ).fit_predict(X)
    
    return labels

def embedding_and_clustering(df, configs):
    
    X, vocab, word2vec_model = get_word2vec(df)
    umap_res = get_umap(X, configs)
    labels = get_hdbscan(umap_res, configs)
    
    skip=0
    limit=100
    
    words = list(vocab)[skip:limit]
    len_data = len(umap_res[:limit])

    i = 0

    plt.figure(figsize=(15, 15))
    while i < len_data:
        plt.scatter(umap_res[i][0], umap_res[i][1], c=labels[i], marker="*", s=500)
        plt.annotate(words[i], (umap_res[i][0], umap_res[i][1]), size=12)
 
        i += 1
    
    return umap_res, words, labels
    
    