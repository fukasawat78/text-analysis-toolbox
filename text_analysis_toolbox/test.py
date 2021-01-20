import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm_notebook as tqdm
import japanize_matplotlib
from text_data_dashboard import TextDataDashboard

if __name__=="__main__":
    df = pd.read_csv("../data/dataset.csv", encoding="utf-8-sig", index_col=0)
    tdd = TextDataDashboard()
    df = tdd.transform(df)
    tdd.create_dashboard(df)