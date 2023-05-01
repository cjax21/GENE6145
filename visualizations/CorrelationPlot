# import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
from data_source import test_rows_labels
data = test_rows_labels
df = pd.read_csv(data)

# df = pd.read_csv(fp + "test_rows_labels.csv", sep = "\t")

# Compute the correlation matrix
corr_matrix = df.iloc[:, 1:].corr()

# Create a heatmap of the correlation matrix
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, cmap='coolwarm', center=0, annot=True, ax=ax)

# Set the plot title
ax.set_title('Correlation Matrix of Gene Features')

# Show the plot
plt.show()