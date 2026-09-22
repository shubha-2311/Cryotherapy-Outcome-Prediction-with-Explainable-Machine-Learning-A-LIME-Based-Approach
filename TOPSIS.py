import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Define mean data from LaTeX table
data = {
    'Model': ['KNN', 'MLP', 'SVM', 'RF'],
    'Accuracy': [90.00, 93.33, 88.89, 94.45],
    'Recall': [86.50, 93.33, 89.33, 92.00],
    'Specificity': [93.00, 93.00, 91.33, 97.50],
    'Precision': [93.83, 95.14, 92.64, 98.33],
    'F1-score': [89.20, 93.40, 89.48, 94.37],
    'GM': [89.21, 92.44, 89.31, 94.29],
    'FPR': [7.00, 7.00, 8.60, 2.50],  # Cost criterion
    'MCC': [80.78, 87.35, 80.34, 90.23],
    'KAPPA': [79.37, 85.73, 77.57, 89.02]
}

df = pd.DataFrame(data)
models = df['Model'].values

# Separate features and mark cost criterion (FPR)
features = df.drop('Model', axis=1)
benefit_criteria = ['Accuracy', 'Recall', 'Specificity', 'Precision',
                    'F1-score', 'GM', 'MCC', 'KAPPA']
cost_criteria = ['FPR']

# Normalize data
scaler = MinMaxScaler()
normalized = scaler.fit_transform(features)
norm_df = pd.DataFrame(normalized, columns=features.columns)

# Invert cost criteria
for col in cost_criteria:
    norm_df[col] = 1 - norm_df[col]

# Assign equal weights to all criteria
weights = np.ones(norm_df.shape[1]) / norm_df.shape[1]

# Weighted normalized decision matrix
weighted = norm_df * weights

# Determine ideal and negative-ideal solutions
ideal = weighted.max()
negative_ideal = weighted.min()

# Distance to ideal and negative-ideal
d_pos = np.linalg.norm(weighted - ideal, axis=1)
d_neg = np.linalg.norm(weighted - negative_ideal, axis=1)

# Calculate closeness
closeness = d_neg / (d_pos + d_neg)

# Attach TOPSIS scores and ranking
df['TOPSIS Score'] = closeness
df['Rank'] = df['TOPSIS Score'].rank(ascending=False).astype(int)

# Sort and print
result = df[['Model', 'TOPSIS Score', 'Rank']].sort_values(by='Rank')
print(result)
