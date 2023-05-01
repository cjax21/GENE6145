import pandas as pd
from pandas.core.frame import DataFrame



def extract_data(filepath: str):
    '''
    extracts csv data and converts to pandas Dataframe
    args:
        file_path (str): path to the csv file
    
    returns:
        df (DataFrame): pandas dataframe containing the csv data
    '''
    df = pd.read_csv(filepath)
    
    return df

def transform(df: DataFrame) -> DataFrame:
    '''
    cleans data

    args:
        df (DataFrame): pandas dataframe containing the raw data
    
    returns:
        df (DataFrame): pandas dataframe containing the clean data
    '''

    # drop null values
    df.dropna(inplace=True)

    # remove decimal from year column and convert to string
    df.Year = df.Year.astype('int').astype("str")
    
    return df