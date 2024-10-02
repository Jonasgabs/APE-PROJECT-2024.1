
import pandas as pd



df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
graus = []
for index, linha in df.iterrows():
    if linha['DS_GRAU_INSTRUCAO'] not in graus:
        graus.append(linha['DS_GRAU_INSTRUCAO'])

print(graus)
