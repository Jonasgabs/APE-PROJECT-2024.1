import pandas as pd

class Main():

    def municipios_cargos(self, municipio, cargo):
        municipio = str(municipio).strip()
        cargo = str(cargo).strip()  

        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['CD_CARGO'] = self.df['CD_CARGO'].astype(str).str.strip()
        self.df['SG_UE'] = self.df['SG_UE'].astype(str).str.strip()

        self.df_filtrados = self.df.loc[
            (self.df['CD_CARGO'] == f'{cargo}') &
            (self.df['SG_UE'] ==  f'{municipio}')
            ]
        
        self.colunas_necessarias = ['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NM_CANDIDATO']
        self.df_filtrados_colunas = self.df_filtrados.loc[:, self.colunas_necessarias]

        print(self.df_filtrados_colunas)

