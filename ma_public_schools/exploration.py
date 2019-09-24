import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# https://www.kaggle.com/ndalziel/massachusetts-public-schools-data/downloads/massachusetts-public-schools-data.zip/1
df_school = pd.read_csv('MA_Public_Schools_2017.csv')
df_school_subset = df_school[['TOTAL_Enrollment', '% White', 'Average Salary', 'Average Class Size',
                              '% Dropped Out', '% MCAS_3rdGrade_Math_P+A', '% MCAS_7thGrade_Math_P+A',
                              '% MCAS_10thGrade_Math_P+A', 'Progress and Performance Index (PPI) - All Students']]

df_school_subset = df_school_subset.fillna(df_school_subset.mean())

corr = df_school_subset.corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
plt.show()
