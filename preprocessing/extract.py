import pandas as pd

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