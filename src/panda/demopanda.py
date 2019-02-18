from pandas import DataFrame, read_csv
import pandas as pd 
 
file = r'D:/0121.csv'
# df = pd.read_csv(file)
# print(df)
# print('Max', df['Highscore'].max())
# print('Min', df['Highscore'].min())

file = r'D:/0121.csv'
df = pd.read_csv(file,header=None)
print(df)