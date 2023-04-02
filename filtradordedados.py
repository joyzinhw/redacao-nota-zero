import pandas as pd
import numpy as np
import matplotlib as plt


tabela = pd.read_excel("essay-br.xlsx", engine='openpyxl')

filtrados = tabela['score'] == 0


pd.get_option('display.max_rows')
pd.set_option('display.max_row', 100)

print("dados filtrados:")
print(tabela[filtrados])

tabela[filtrados].to_excel('filtrados.xlsx', index=False)
