import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Sequence, Literal, List, Union, Iterable
import pandas as pd



def EncodingPlot(dataframe: Literal[pd.DataFrame], strategy=Union[str,None], n_bins: int, pallette):
    idx = dataframe.columns.get_loc('age')
    encoder = ColumnTransformer(transformers = [
        ("equalwidth", KBinsDiscretizer(strategy = strategy, n_bins=n_bins, encode = "ordinal"), [idx])
    ])
    background_color = "#f6f5f5"
    
    plt.figure(figsize=(10,6), facecolor='#f6f5f5')

    plt.subplot(1,2,1)
    sns.histplot(data = dataframe["age"], color="#D6265D", legend=False)
    plt.xlabel("AGE")
    plt.ylabel("")
    plt.title("Before Binnning")

    plt.subplot(1,2,2)
    sns.histplot(data = encoder.transform(dataframe), palette=pallette, legend=False)
    plt.xlabel("AGE")
    plt.ylabel("")
    plt.title("After Binning")
    
    plt.savefig(strategy+'_plot.pdf', dpi = 330)
    
    plt.show()