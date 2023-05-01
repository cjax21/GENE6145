import pandas as pd
from pandas.core.frame import DataFrame
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Sequence, Literal, List, Union, Iterable
import pandas as pd



def EncoderPlot(dataframe: DataFrame, strategy=Union[Literal[str],None], n_bins: int, pallette=):
    """
    EncoderPlot returns the transformed sparse matrix of the 

    Parameters
    ----------
    dataframe : Literal[pd.DataFrame]
        _description_
    n_bins : int
        _description_
    pallette : _type_
        _description_
    strategy : _type_, optional
        _description_, by default Union[str,None]

    Returns
    -------
    _type_
        _description_
    """
    
    
    
    
    idx = dataframe.columns.get_loc('age')
    encoder = ColumnTransformer(transformers = [
        ("equalwidth", KBinsDiscretizer(strategy = strategy, n_bins=n_bins, encode = "ordinal", random_state=42), [idx])
    ])
    
    data = encoder.transform(dataframe)
    face_color = "#f6f5f5" #background color
    
    plt.figure(figsize=(10,6), facecolor=face_color)

    plt.subplot(1,2,1)
    sns.histplot(data = dataframe["age"], color="#D6265D", legend=False)
    plt.xlabel("AGE")
    plt.ylabel("")
    plt.title("Before Binnning")

    plt.subplot(1,2,2)
    sns.histplot(data = data, palette=pallette, legend=False)
    plt.xlabel("AGE")
    plt.ylabel("")
    plt.title("After Binning")
    
    plt.savefig('encoded_plot.pdf', dpi = 330)
    
    plt.show()
    
    return data