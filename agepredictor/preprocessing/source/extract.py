import pandas as pd
from genpipes import declare

rnaseq = "https://zenodo.org/record/2545213/files/training_data_normal.tsv"
methylation_train_rows = "https://zenodo.org/record/2545213/files/train_rows.csv"
methylation_test_rows_labels = (
    "https://zenodo.org/record/2545213/files/test_rows_labels.csv"
)
methylation_test_rows = "https://zenodo.org/record/2545213/files/test_rows.csv"

@declare.generator()
@declare.datasource(inputs=rnaseq)
def rnaseq_df(filepath: str) -> pd.DataFrame:
    """
    extracts csv data,  converts to pandas Dataframe, 
    performs feature selection with sklearn.SelectKBest and f_regression
    
    args:
        file_path (str): path to the csv file

    returns:
        df (DataFrame): pandas dataframe containing the selected data.
    """
    df = pd.read_csv(filepath)

    return df


@declare.datasource(inputs=methylation_train_rows)
def methylation_train_rows_df(filepath: str) -> pd.DataFrame:
    """
    extracts csv data and converts to pandas Dataframe
    args:
        file_path (str): path to the csv file

    returns:
        df (DataFrame): pandas dataframe containing the csv data
    """
    df = pd.read_csv(filepath)
    new_labels = {'RPA2_3': 'RPA2', 'ZYG11A_4': 'ZYG11A','F5_2': 'F5', 'HOXC4_1': 'HOXC4', 
              'NKIRAS2_2': 'NKIRAS2',	'MEIS1_1' : 'MEIS1',	'SAMD10_2' : 'SAMD10',	'GRM2_9': 'GRM2',
              'TRIM59_5' : 'TRIM59',	'LDB2_3' :	'LDB2', 'ELOVL2_6' : 'ELOVL2', 'DDO_1' : 'DDO',	'KLF14_2' : 'KLF14'}
    df = df.rename(columns=new_labels)
    
    s = f'{df.shape[0]} samples and {df.shape[1]} features'
    print(s)

    return df


@declare.datasource(inputs=methylation_test_rows_labels)
def methylation_test_rows_labels_df(filepath: str) -> pd.DataFrame:
    """
    extracts csv data and converts to pandas Dataframe
    args:
        file_path (str): path to the csv file

    returns:
        df (DataFrame): pandas dataframe containing the csv data
    """
    df = pd.read_csv(filepath)
    # Rename the labels of the first two columns
    new_labels = {'RPA2_3': 'RPA2', 'ZYG11A_4': 'ZYG11A','F5_2': 'F5', 'HOXC4_1': 'HOXC4', 
              'NKIRAS2_2': 'NKIRAS2',	'MEIS1_1' : 'MEIS1',	'SAMD10_2' : 'SAMD10',	'GRM2_9': 'GRM2',
              'TRIM59_5' : 'TRIM59',	'LDB2_3' :	'LDB2', 'ELOVL2_6' : 'ELOVL2', 'DDO_1' : 'DDO',	'KLF14_2' : 'KLF14'}
    df = df.rename(columns=new_labels)
    s = f'{df.shape[0]} samples and {df.shape[1]} features'
    print(s)


    return df


@declare.datasource(inputs=methylation_test_rows)
def methylation_test_rows_df(filepath: str) -> pd.DataFrame:
    """
    extracts csv data and converts to pandas Dataframe
    args:
        file_path (str): path to the csv file

    returns:
        df (DataFrame): pandas dataframe containing the csv data
    """
    df = pd.read_csv(filepath)
    
    # Rename the labels of cols``
    new_labels = {'RPA2_3': 'RPA2', 'ZYG11A_4': 'ZYG11A','F5_2': 'F5', 'HOXC4_1': 'HOXC4', 
              'NKIRAS2_2': 'NKIRAS2',	'MEIS1_1' : 'MEIS1',	'SAMD10_2' : 'SAMD10',	'GRM2_9': 'GRM2',
              'TRIM59_5' : 'TRIM59',	'LDB2_3' :	'LDB2', 'ELOVL2_6' : 'ELOVL2', 'DDO_1' : 'DDO',	'KLF14_2' : 'KLF14'}
    df = df.rename(columns=new_labels)

    s = f'{df.shape[0]} samples and {df.shape[1]} features'
    print(s)

    return df
