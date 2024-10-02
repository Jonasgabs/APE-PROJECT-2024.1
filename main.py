import pandas as pd

class Main():
    #func pra trazer os candidadtos
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

    #func pra trazer os códigos dos municipios
    def pegando_mun(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['SG_UE'] = self.df['SG_UE'].astype(str).str.strip() 
        valores_unicos = self.df['SG_UE'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas

    #func pra trazer os códigos dos cargos
    def pegando_cargo(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['CD_CARGO'] = self.df['CD_CARGO'].astype(str).str.strip() 
        valores_unicos = self.df['CD_CARGO'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas
    
    #func pra trazer os códigos dos candidatos
    def pegando_cod(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['NR_CANDIDATO'] = self.df['NR_CANDIDATO'].astype(str).str.strip()
        valores_unicos = self.df['NR_CANDIDATO'].unique().tolist()
        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        #print(valores_com_aspas)
        return valores_com_aspas

    #func pra trazer os candidatos baseado nos códigos
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

    #func pra trazer a quantidade de prefeitos, vices e vereadores     
    def qtd(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['CD_CARGO'] = self.df['CD_CARGO'].astype(str).str.strip()

        self.df_prefeitos = self.df.loc[
            (self.df['CD_CARGO'] == '11') 
        ]

        self.df_vice = self.df.loc[
            (self.df['CD_CARGO'] == '12') 
        ]

        self.df_vereador = self.df.loc[
            (self.df['CD_CARGO'] == '13') 
        ]
        qtd =[len(self.df_prefeitos), len(self.df_vice), len(self.df_vereador)]

        return qtd
    
    def partido_pref():
        df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        df['CD_CARGO'] = df['CD_CARGO'].astype(str).str.strip()
        df['NM_PARTIDO'] = df['NM_PARTIDO'].astype(str).str.strip()
        df_prefeitos = df.loc[
            (df['CD_CARGO'] == '11')
        ]
        partidos_candidatos = df_prefeitos.groupby('NM_PARTIDO').size().reset_index(name='Quantidade')
        return partidos_candidatos
    
    def faixa_etaria(self):
        qt21 = 0
        qt22_40 = 0
        qt41_60 = 0
        qt61 = 0
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['DT_NASCIMENTO'] = self.df['DT_NASCIMENTO'].astype(str).str.strip()
        self.df['DT_NASCIMENTO'] = pd.to_datetime(self.df['DT_NASCIMENTO'],  format='%d/%m/%Y', errors='coerce')
        self.ano = self.df['DT_NASCIMENTO'].dt.year
        self.ano = self.ano.tolist()
        for i in range(len(self.ano)):
            if (2024 - int(self.ano[i])) <= 21:
                qt21 += 1
            elif (2024 - int(self.ano[i])) <= 40:
                qt22_40 += 1
            elif (2024 - int(self.ano[i])) <= 60:
                qt41_60 += 1
            elif (2024 - int(self.ano[i])) > 60:
                qt61 += 1
        
        return qt21, qt22_40, qt41_60, qt61
    

    def percentuals():
        df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        for index, linha in df.iterrows():
            




        valores_com_aspas = [f'{valor}' for valor in valores_unicos]
        print(valores_com_aspas)
        
  "DS_CARGO"



    "DS_GRAU_INSTRUCAO"

    DS_GENERO
if __name__ == '__main__':
    main = Main()
    main.grau_instrucao()
