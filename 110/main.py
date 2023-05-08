import pandas as pd
import numpy as np
from sklearn.neighbors import LocalOutlierFactor

# target columns no y no2

target_columns = ['FECHA', 'NO', 'NO2']

pla = "data/ElPla-MDEST030140062022.txt"
florida = "data/FloridaBabel-MDEST030140082022.txt"
rabasa = "data/Rabasa-MDEST030140092022.txt"

def read_file(file):
  df = pd.read_csv(file, sep='\t', decimal=',', skiprows=[0, 1, 2, 4], encoding = "ISO-8859-1")
  return df

df_pla = read_file(pla)
df_florida = read_file(florida)
df_rabasa = read_file(rabasa)


df_pla_target = df_pla[target_columns]
df_florida_target = df_florida[target_columns]

# merged = pd.concat([
#   df_pla[target_columns], 
#   df_florida[target_columns], 
#   df_rabasa[target_columns]
# ], axis=1)

merged = df_pla_target.merge(df_florida_target, left_on="FECHA", right_on="FECHA").merge(df_rabasa[target_columns], left_on="FECHA", right_on="FECHA")

merged.rename(columns={
  'NO_x': "PLA_NO",
  'NO2_x': "PLA_NO2",
  'NO_y': "FLORIDA_NO",
  'NO2_y': "FLORIDA_NO2",
  'NO': "RABASA_NO",
  'NO2': "RABASA_NO2",
}, inplace=True)

merged.fillna(0, inplace=True)


merged_no = merged[["PLA_NO", "FLORIDA_NO", "RABASA_NO"]]

# print(df_pla.count())
# print(df_florida.count())
# print(df_rabasa.count())

clf = LocalOutlierFactor(n_neighbors=2)
clf.fit_predict(merged_no)
print(clf.negative_outlier_factor_)
print(merged_no.head(8))
