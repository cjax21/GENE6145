# import libraries
import pandas as pd 
from pandas.core.frame import DataFrame
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from extract import extract_data
from typing import Union, AnyStr

# Load dataset
from preprocessing.extract import extract_data
data = 'https://github.com/cjax21/GENE6145/blob/main/data_source/test_rows_labels.csv'
df = extract_data(data)

df = pd.read_csv(fp + "test_rows_labels.csv", sep = "\t")
# Rename the labels
new_labels = {'RPA2_3': 'RPA2', 'ZYG11A_4': 'ZYG11A','F5_2': 'F5', 'HOXC4_1': 'HOXC4', 
              'NKIRAS2_2': 'NKIRAS2',	'MEIS1_1' : 'MEIS1',	'SAMD10_2' : 'SAMD10',	'GRM2_9': 'GRM2',
              'TRIM59_5' : 'TRIM59',	'LDB2_3' :	'LDB2', 'ELOVL2_6' : 'ELOVL2', 'DDO_1' : 'DDO',	'KLF14_2' : 'KLF14'}
df = df.rename(columns=new_labels)

# Define the target variable
target = 'Age'

# Define the number of columns in the subplot grid
num_cols = 4

# Calculate the number of rows needed to display all scatter plots
num_rows = len(df.columns[:13]) // num_cols + 1

# Define the list of colors
colors = ['#7AD151FF' if i+1 in [1, 2, 4, 8, 9, 11, 13] else '#440154FF' for i in range(len(df.columns[:]))]

# Create a figure with a subplot grid
fig, axes = plt.subplots(num_rows, num_cols, figsize=(16, 8))

# Loop through each gene feature and create a scatter plot in a separate subplot
for i, col in enumerate(df.columns[:13]):
    row_idx = i // num_cols
    col_idx = i % num_cols
    axes[row_idx, col_idx].scatter(df[col], df[target], color=colors[i])
    axes[row_idx, col_idx].set_xlabel(col)
    axes[row_idx, col_idx].set_ylabel(target)
    axes[row_idx, col_idx].set_title(f'{col}')

# Hide the empty subplots
for i in range(len(df.columns[:13]), num_rows*num_cols):
    row_idx = i // num_cols
    col_idx = i % num_cols
    axes[row_idx, col_idx].axis('off')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()