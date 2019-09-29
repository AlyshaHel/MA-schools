import logging
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# https://www.kaggle.com/ndalziel/massachusetts-public-schools-data/downloads/massachusetts-public-schools-data.zip/1
df_school = pd.read_csv('MA_Public_Schools_2017.csv')
# df_school_subset = df_school[['TOTAL_Enrollment', '% White', 'Average Salary', 'Average Class Size',
#                               '% Dropped Out', '% MCAS_3rdGrade_Math_P+A', '% MCAS_7thGrade_Math_P+A',
#                               '% MCAS_10thGrade_Math_P+A', 'Progress and Performance Index (PPI) - All Students']]

df_school_subset = df_school.iloc[:, 15:]
print(df_school_subset.shape)
df_school_subset_cols = df_school_subset.columns
df_full_values = (df_school_subset.isna().sum() * 100 / df_school_subset.shape[0]).values
print(df_full_values)
for i in range(len(df_full_values)):
    if df_full_values[i] > 50.0:
        label = df_school_subset_cols[i]
        df_school_subset.drop(labels=label, axis=1)
print(df_school_subset.shape)

df_school_subset = df_school_subset.fillna(df_school_subset.mean())

corr = df_school_subset.corr()
avg_salary = corr.loc['Average Salary']

data_salary_corr = []
for i in avg_salary.index:
    if 0.25 <= abs(avg_salary.loc[i]) < 1:
        item = [i, avg_salary.loc[i]]
        data_salary_corr.append(item)
df_salary = pd.DataFrame(data_salary_corr, columns=['Metric', 'Correlation'])
plt.barh(df_salary.Metric, df_salary.Correlation, align='center', alpha=0.5)
# plt.show()

# ax = sns.heatmap(
#     corr,
#     vmin=-1, vmax=1, center=0,
#     cmap=sns.diverging_palette(20, 220, n=200),
#     square=True
# )
# ax.set_xticklabels(
#     ax.get_xticklabels(),
#     rotation=45,
#     horizontalalignment='right'
# )
# plt.show()
