# How to create a tabular file.
import pandas as pd

arquivo = pd.read_csv('http://bit.ly/chiporders', sep='\t')

print(arquivo)
