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

    def pegando_mun(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['SG_UE'] = self.df['SG_UE'].astype(str).str.strip() 
        valores_unicos = self.df['SG_UE'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas

    def pegando_cargo(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['CD_CARGO'] = self.df['CD_CARGO'].astype(str).str.strip() 
        valores_unicos = self.df['CD_CARGO'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas
    
    def pegando_cod(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['NR_CANDIDATO'] = self.df['NR_CANDIDATO'].astype(str).str.strip()
        valores_unicos = self.df['NR_CANDIDATO'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas

    def cod_candidatos(self, codigo):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['NR_CANDIDATO'] = self.df['NR_CANDIDATO'].astype(str).str.strip()
        self.df_candidato = self.df.loc[self.df['NR_CANDIDATO'] == f'{codigo}']
        self.colunas_necessarias = ['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NM_CANDIDATO', 'NM_PARTIDO']
        self.df_filtrados_colunas = self.df_candidato.loc[:, self.colunas_necessarias]
        candidatos_concatenados = self.df_filtrados_colunas.apply(
            lambda row: f"{row['NM_URNA_CANDIDATO']} ; Número candidato: {row['NR_CANDIDATO']} ; Nome candidato: {row['NM_CANDIDATO']} ; Partido: {row['NM_PARTIDO']}", axis=1
        )
        for candidato in candidatos_concatenados:
            print(candidato)

if __name__ == '__main__':
    main = Main()
    main.cod_candidatos()