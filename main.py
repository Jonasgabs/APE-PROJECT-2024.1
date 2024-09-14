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
        
        self.colunas_necessarias = ['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NM_CANDIDATO', 'NM_PARTIDO']
        self.df_filtrados_colunas = self.df_filtrados.loc[:, self.colunas_necessarias]

        candidatos_concatenados = self.df_filtrados_colunas.apply(
            lambda row: f"{row['NM_URNA_CANDIDATO']} ; {row['NR_CANDIDATO']} ; {row['NM_CANDIDATO']} ; {row['NM_PARTIDO']}", axis=1
        )

        return candidatos_concatenados.tolist()

    def cod_candidatos(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        valores_unicos = self.df['NR_CANDIDATO'].unique().tolist() 
        print(valores_unicos)

if __name__ == '__main__':
    main = Main()
    main.cod_candidatos()