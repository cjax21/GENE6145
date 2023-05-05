# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
from  source.extract import  
data = test_rows_labels
df = pd.read_csv(data)

# df = pd.read_csv(fp + "test_rows_labels.csv", sep = "\t")

# Rename the labels of the first two columns
new_labels = {'RPA2_3': 'RPA2', 'ZYG11A_4': 'ZYG11A','F5_2': 'F5', 'HOXC4_1': 'HOXC4', 
              'NKIRAS2_2': 'NKIRAS2',	'MEIS1_1' : 'MEIS1',	'SAMD10_2' : 'SAMD10',	'GRM2_9': 'GRM2',
              'TRIM59_5' : 'TRIM59',	'LDB2_3' :	'LDB2', 'ELOVL2_6' : 'ELOVL2', 'DDO_1' : 'DDO',	'KLF14_2' : 'KLF14'}
df = df.rename(columns=new_labels)

# Compute the correlation matrix
corr_matrix = df.iloc[:, :].corr()

# Create a heatmap of the correlation matrix
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, cmap='viridis', center=0, annot=True,
            xticklabels=corr_matrix.columns.values,
            yticklabels=corr_matrix.columns.values, ax=ax)

# Set the plot title
ax.set_title('Correlation Matrix of Gene Features')

# Rotate x-axis label 45 degrees
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

# Show the plot
plt.show()