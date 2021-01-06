import gensim

# https://drive.google.com/file/d/0ByFQ96A4DgSPUm9wVWRLdm5qbmc/view

def get_polarity_dict(self, path):
    #dicというディレクトリにダウンロードしてきた極性辞書を入れておく
    # http://www.lr.pi.titech.ac.jp/~takamura/pndic_ja.html
    p_dic = pathlib.Path(path)

    for i in p_dic.glob('*.txt'):
        with open (i, 'r', encoding = 'utf-8') as f:
            x = [ii.replace('\n', '').split(':') for ii in  f.readlines()]

    pos_neg_df = pd.DataFrame(x, columns = ['基本形', '読み', '品詞', 'スコア'])
    #jaconvを使って読み仮名を全てカタカナに変換
    pos_neg_df['読み'] = pos_neg_df['読み'].apply(lambda x : jaconv.hira2kata(x))
    #なぜか読みや品詞まで同じなのに、異なるスコアが割り当てられていたものがあったので重複を削除
    pos_neg_df = pos_neg_df[~pos_neg_df[['基本形', '読み', '品詞']].duplicated()]
    
    return pos_neg_df

def wiki_model(x, model, pos_list, neg_list):

    pos = []
    for i in pos_list:
        try:
            n = model.similarity(i, x)
            pos.append(n)
        except:
            continue
    try:
        pos_mean = sum(pos)/len(pos)
    except:
        pos_mean = 0

    #ネガティブ度合いの判定
    neg = []
    for i in neg_list:
        try:
            n = model.similarity(i, x)
            neg.append(n)
        except:
            continue
    try:
        neg_mean = sum(neg)/len(neg)
    except:
        neg_mean = 0
    if pos_mean > neg_mean:
        return pos_mean
    if neg_mean > pos_mean:
        return -neg_mean
    else:
        return 0