# import libraries
import pandas as pd 
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from extract import extract_data

# Load dataset
from preprocessing.extract import extract_data
data = 'https://github.com/cjax21/GENE6145/blob/main/data_source/test_rows_labels.csv'
df = extract_data(data)

# Define the target variable
target = 'Age'

# Loop through each gene feature and create a scatter plot
for col in df.columns[1:]:
    plt.figure()
    plt.scatter(df[col], df[target])
    plt.xlabel(col)
    plt.ylabel(target)
    plt.title(f'Scatter Plot of {col} vs. {target}')
    plt.show()

# Wrap plots by columns of 4
# Define the number of columns in the subplot grid
num_cols = 4

# Calculate the number of rows needed to display all scatter plots
num_rows = len(df.columns[1:]) // num_cols + 1

# Create a figure with a subplot grid
fig, axes = plt.subplots(num_rows, num_cols, figsize=(16, 8))

# Loop through each gene feature and create a scatter plot in a separate subplot
for i, col in enumerate(df.columns[1:]):
    row_idx = i // num_cols
    col_idx = i % num_cols
    axes[row_idx, col_idx].scatter(df[col], df[target])
    axes[row_idx, col_idx].set_xlabel(col)
    axes[row_idx, col_idx].set_ylabel(target)
    axes[row_idx, col_idx].set_title(f'Scatter Plot of {col} vs. {target}')

# Hide the empty subplots
for i in range(len(df.columns[1:]), num_rows*num_cols):
    row_idx = i // num_cols
    col_idx = i % num_cols
    axes[row_idx, col_idx].axis('off')

# Adjust the spacing between subplots
fig.tight_layout()

# Show the plot
plt.show()