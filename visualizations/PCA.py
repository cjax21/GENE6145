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

# df = pd.read_csv(fp + "test_rows_labels.csv", sep = "\t")
# df

# Define age groups based on age values
age_groups = pd.cut(df['Age'], [0, 34, 55, np.inf], labels=['Adult', 'Middle-aged', 'Elderly'])

# Perform PCA on the gene features
pca = PCA(n_components=2)
principal_components = pca.fit_transform(df.iloc[:, 1:])

# Get the explained variance ratio
explained_var_ratio = pca.explained_variance_ratio_

# Create a new DataFrame with the principal components and age groups
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['Age Group'] = age_groups.values

# Plot the PCA, colored by age group
fig, ax = plt.subplots()
colors = {'Adult': 'red', 'Middle-aged': 'green', 'Elderly': 'blue'}
for age_group, color in colors.items():
    mask = pca_df['Age Group'] == age_group
    ax.scatter(pca_df.loc[mask, 'PC1'], pca_df.loc[mask, 'PC2'], c=color, label=age_group, alpha=0.5)

# Add axis labels and legend
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.legend()

# Show the plot
plt.show()

# Print the explained variance ratio
print('Explained variance ratio:', explained_var_ratio)