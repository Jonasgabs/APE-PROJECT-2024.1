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
        self.colunas_necessarias = ['NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NM_CANDIDATO', 'NM_PARTIDO' ,'SQ_CANDIDATO']
        self.df_filtrados_colunas = self.df_candidato.loc[:, self.colunas_necessarias]
        candidatos_concatenados = self.df_filtrados_colunas.apply(
            lambda row: f"{row['NM_URNA_CANDIDATO']},{row['NR_CANDIDATO']},{row['NM_CANDIDATO']},{row['NM_PARTIDO']},{row['SQ_CANDIDATO']}", axis=1
        )
        return candidatos_concatenados

    #func pra trazer a quantidade de prefeitos, vices e vereadores     
    def qtd(self):
        df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        df['CD_CARGO'] = df['CD_CARGO'].astype(str).str.strip()

        df_prefeitos = df.loc[
            (df['CD_CARGO'] == '11') 
        ]

        df_vice = df.loc[
            (df['CD_CARGO'] == '12') 
        ]

        df_vereador = df.loc[
            (df['CD_CARGO'] == '13') 
        ]
        qtd =[len(df_prefeitos), len(df_vice), len(df_vereador)]

        return qtd
    
    def partido_pref(self):
        self.df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        self.df['CD_CARGO'] = self.df['CD_CARGO'].astype(str).str.strip()
        self.df['NM_PARTIDO'] = self.df['NM_PARTIDO'].astype(str).str.strip()
        self.df_prefeitos = self.df.loc[
            (self.df['CD_CARGO'] == '11')
        ]
        partidos_candidatos = self.df_prefeitos.groupby('NM_PARTIDO').size().reset_index(name='Quantidade')
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
    
        
    def percentuals(self):
        total_candidatos = sum(self.faixa_etaria())
        df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
        LeE = EfI = EfC = EmI = EmC = Si = Sc = 0
        genero_F = genero_M = 0
        casado = solteiro = divorciado = viuvo = separado = 0
        #prefeitos
        qtd_prefeitos = 0
        prefeito_LeE = prefeito_EfI = prefeito_EfC = prefeito_EmI = prefeito_EmC = prefeito_Si = prefeito_Sc = 0
        prefeito_genero_F = prefeito_genero_M = 0
        prefeito_casado = prefeito_solteiro = prefeito_divorciado = prefeito_viuvo = prefeito_separado = 0
        #vice
        qtd_vice = 0
        viceprefeito_LeE = viceprefeito_EfI = viceprefeito_EfC = viceprefeito_EmI = viceprefeito_EmC = viceprefeito_Si = viceprefeito_Sc = 0
        viceprefeito_genero_F = viceprefeito_genero_M = 0
        viceprefeito_casado = viceprefeito_solteiro = viceprefeito_divorciado = viceprefeito_viuvo = viceprefeito_separado =  0
        #vereadores
        qtd_vereadores = 0
        vereador_LeE = vereador_EfI = vereador_EfC = vereador_EmI = vereador_EmC = vereador_Si = vereador_Sc = 0
        vereador_genero_F = vereador_genero_M = 0
        vereador_casado = vereador_solteiro = vereador_divorciado = vereador_viuvo = vereador_separado = 0


        for index, linha in df.iterrows():
            if linha["DS_CARGO"] == "PREFEITO":
                qtd_prefeitos += 1

                match linha["DS_GRAU_INSTRUCAO"]:
                    case 'LÊ E ESCREVE':
                        prefeito_LeE += 1
                        LeE += 1
                    case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        prefeito_EfI += 1
                        EfI += 1
                    case 'ENSINO FUNDAMENTAL COMPLETO':
                        prefeito_EfC += 1
                        EfC += 1
                    case 'ENSINO MÉDIO INCOMPLETO':
                        prefeito_EmI += 1
                        EmI += 1
                    case 'ENSINO MÉDIO COMPLETO':
                        prefeito_EmC += 1
                        EmC += 1 
                    case 'SUPERIOR INCOMPLETO':
                        prefeito_Si += 1
                        Si += 1
                    case 'SUPERIOR COMPLETO':
                        prefeito_Sc += 1
                        Sc += 1
                
                if linha["DS_GENERO"] == 'MASCULINO':
                    prefeito_genero_M += 1
                    genero_M += 1
                elif linha["DS_GENERO"] == 'FEMININO':
                    prefeito_genero_F += 1
                    genero_F += 1

                match linha["DS_ESTADO_CIVIL"]:
                    case 'CASADO(A)':
                        prefeito_casado += 1
                        casado += 1
                    case 'SOLTEIRO(A)':
                        prefeito_solteiro += 1
                        solteiro += 1
                    case 'DIVORCIADO(A)':
                        prefeito_divorciado += 1
                        divorciado += 1
                    case 'VIÚVO(A)':
                        prefeito_viuvo += 1
                        viuvo += 1

                    case 'SEPARADO(A) JUDICIALMENTE':
                        prefeito_separado += 1
                        separado += 1

            elif linha["DS_CARGO"] == "VICE-PREFEITO":
                
                qtd_vice += 1
                match linha["DS_GRAU_INSTRUCAO"]:
                    case 'LÊ E ESCREVE':
                        viceprefeito_LeE += 1
                        LeE += 1
                    case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        viceprefeito_EfI += 1
                        EfI += 1
                    case 'ENSINO FUNDAMENTAL COMPLETO':
                        viceprefeito_EfC += 1
                        EfC += 1
                    case 'ENSINO MÉDIO INCOMPLETO':
                        viceprefeito_EmI += 1
                        EmI += 1
                    case 'ENSINO MÉDIO COMPLETO':
                        viceprefeito_EmC += 1
                        EmC += 1 
                    case 'SUPERIOR INCOMPLETO':
                        viceprefeito_Si += 1
                        Si += 1
                    case 'SUPERIOR COMPLETO':
                        viceprefeito_Sc += 1
                        Sc += 1
                
                if linha["DS_GENERO"] == 'MASCULINO':
                    viceprefeito_genero_M += 1
                    genero_M += 1
                elif linha["DS_GENERO"] == 'FEMININO':
                    viceprefeito_genero_F += 1
                    genero_F += 1

                match linha["DS_ESTADO_CIVIL"]:
                    case 'CASADO(A)':
                        viceprefeito_casado += 1
                        casado += 1
                    case 'SOLTEIRO(A)':
                        viceprefeito_solteiro += 1
                        solteiro += 1
                    case 'DIVORCIADO(A)':
                        viceprefeito_divorciado += 1
                        divorciado += 1
                    case 'VIÚVO(A)':
                        viceprefeito_viuvo += 1
                        viuvo += 1
                    case 'SEPARADO(A) JUDICIALMENTE':
                        viceprefeito_separado += 1
                        separado += 1
            
            elif linha["DS_CARGO"] == "VEREADOR":
                qtd_vereadores += 1

                match linha["DS_GRAU_INSTRUCAO"]:
                    case 'LÊ E ESCREVE':
                        vereador_LeE += 1
                        LeE += 1
                    case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        vereador_EfI += 1
                        EfI += 1
                    case 'ENSINO FUNDAMENTAL COMPLETO':
                        vereador_EfC += 1
                        EfC += 1
                    case 'ENSINO MÉDIO INCOMPLETO':
                        vereador_EmI += 1
                        EmI += 1
                    case 'ENSINO MÉDIO COMPLETO':
                        vereador_EmC += 1
                        EmC += 1 
                    case 'SUPERIOR INCOMPLETO':
                        vereador_Si += 1
                        Si += 1
                    case 'SUPERIOR COMPLETO':
                        vereador_Sc += 1
                        Sc += 1
                
                if linha["DS_GENERO"] == 'MASCULINO':
                    vereador_genero_M += 1
                    genero_M += 1
                elif linha["DS_GENERO"] == 'FEMININO':
                    vereador_genero_F += 1
                    genero_F += 1

                match linha["DS_ESTADO_CIVIL"]:
                    case 'CASADO(A)':
                        vereador_casado += 1
                        casado += 1
                    case 'SOLTEIRO(A)':
                        vereador_solteiro += 1
                        solteiro += 1
                    case 'DIVORCIADO(A)':
                        vereador_divorciado += 1
                        divorciado += 1
                    case 'VIÚVO(A)':
                        vereador_viuvo += 1
                        viuvo += 1
                    case 'SEPARADO(A) JUDICIALMENTE':
                        vereador_separado += 1
                        separado += 1




        #porcentagens prefeito
        porcentagens_prefeito = []
        porcentagem_prefeito = (qtd_prefeitos / total_candidatos) * 100
        porcentagens_prefeito.append(porcentagem_prefeito)
        porcentagem_prefeito_LeE, porcentagem_prefeito_EfI, porcentagem_prefeito_EfC, porcentagem_prefeito_EmI, porcentagem_prefeito_EmC, porcentagem_prefeito_Si, porcentagem_prefeito_Sc = (prefeito_LeE / qtd_prefeitos) * 100, (prefeito_EfI / qtd_prefeitos) * 100, (prefeito_EfC / qtd_prefeitos) * 100, (prefeito_EmI / qtd_prefeitos) * 100, (prefeito_EmC / qtd_prefeitos) * 100, (prefeito_Si / qtd_prefeitos) * 100, (prefeito_Sc / qtd_prefeitos) * 100
        porcentagens_prefeito += [porcentagem_prefeito_LeE, porcentagem_prefeito_EfI, porcentagem_prefeito_EfC, porcentagem_prefeito_EmI, porcentagem_prefeito_EmC, porcentagem_prefeito_Si, porcentagem_prefeito_Sc]
        porcentagem_prefeito_genero_F, porcentagem_prefeito_genero_M = (prefeito_genero_F / qtd_prefeitos) * 100, (prefeito_genero_M / qtd_prefeitos) * 100
        porcentagens_prefeito += [porcentagem_prefeito_genero_F, porcentagem_prefeito_genero_M]
        porcentagem_prefeito_casado, porcentagem_prefeito_solteiro, porcentagem_prefeito_divorciado, porcentagem_prefeito_viuvo = (prefeito_casado / qtd_prefeitos) * 100, (prefeito_solteiro / qtd_prefeitos) * 100, (prefeito_divorciado / qtd_prefeitos) * 100, (prefeito_viuvo / qtd_prefeitos) * 100
        porcentagens_prefeito += [porcentagem_prefeito_casado, porcentagem_prefeito_solteiro, porcentagem_prefeito_divorciado, porcentagem_prefeito_viuvo]
        porcentagens_prefeito += [(prefeito_separado / qtd_prefeitos) * 100]

        #porcentagens viceprefeito
        porcentagens_viceprefeito = []
        porcentagem_viceprefeito = (qtd_vice / total_candidatos) * 100
        porcentagens_viceprefeito.append(porcentagem_viceprefeito)
        porcentagem_viceprefeito_LeE, porcentagem_viceprefeito_EfI, porcentagem_viceprefeito_EfC, porcentagem_viceprefeito_EmI, porcentagem_viceprefeito_EmC, porcentagem_viceprefeito_Si, porcentagem_viceprefeito_Sc = (viceprefeito_LeE / qtd_vice) * 100, (viceprefeito_EfI / qtd_vice) * 100, (viceprefeito_EfC / qtd_vice) * 100, (viceprefeito_EmI / qtd_vice) * 100, (viceprefeito_EmC / qtd_vice) * 100, (viceprefeito_Si / qtd_vice) * 100, (viceprefeito_Sc / qtd_vice) * 100
        porcentagens_viceprefeito += [porcentagem_viceprefeito_LeE, porcentagem_viceprefeito_EfI, porcentagem_viceprefeito_EfC, porcentagem_viceprefeito_EmI, porcentagem_viceprefeito_EmC, porcentagem_viceprefeito_Si, porcentagem_viceprefeito_Sc]
        porcentagem_viceprefeito_genero_F, porcentagem_viceprefeito_genero_M = (viceprefeito_genero_F / qtd_vice) * 100, (viceprefeito_genero_M / qtd_vice) * 100
        porcentagens_viceprefeito += [porcentagem_viceprefeito_genero_F, porcentagem_viceprefeito_genero_M]
        porcentagem_viceprefeito_casado, porcentagem_viceprefeito_solteiro, porcentagem_viceprefeito_divorciado, porcentagem_viceprefeito_viuvo = (viceprefeito_casado / qtd_vice) * 100, (viceprefeito_solteiro / qtd_vice) * 100, (viceprefeito_divorciado / qtd_vice) * 100, (viceprefeito_viuvo / qtd_vice) * 100
        porcentagens_viceprefeito += [porcentagem_viceprefeito_casado, porcentagem_viceprefeito_solteiro, porcentagem_viceprefeito_divorciado, porcentagem_viceprefeito_viuvo]
        porcentagens_viceprefeito += [(viceprefeito_separado/ qtd_vice) * 100]

        #porcentagens vereador
        porcentagens_vereador = []
        porcentagem_vereador = (qtd_vereadores / total_candidatos) * 100
        porcentagens_vereador.append(porcentagem_vereador)
        porcentagem_vereador_LeE, porcentagem_vereador_EfI, porcentagem_vereador_EfC, porcentagem_vereador_EmI, porcentagem_vereador_EmC, porcentagem_vereador_Si, porcentagem_vereador_Sc = (vereador_LeE / qtd_vereadores) * 100, (vereador_EfI / qtd_vereadores) * 100, (vereador_EfC / qtd_vereadores) * 100, (vereador_EmI / qtd_vereadores) * 100, (vereador_EmC / qtd_vereadores) * 100, (vereador_Si / qtd_vereadores) * 100, (vereador_Sc / qtd_vereadores) * 100
        porcentagens_vereador += [porcentagem_vereador_LeE, porcentagem_vereador_EfI, porcentagem_vereador_EfC, porcentagem_vereador_EmI, porcentagem_vereador_EmC, porcentagem_vereador_Si, porcentagem_vereador_Sc]
        porcentagem_vereador_genero_F, porcentagem_vereador_genero_M = (vereador_genero_F / qtd_vereadores) * 100, (vereador_genero_M / qtd_vereadores) * 100
        porcentagens_vereador += [porcentagem_vereador_genero_F, porcentagem_vereador_genero_M]
        porcentagem_vereador_casado, porcentagem_vereador_solteiro, porcentagem_vereador_divorciado, porcentagem_vereador_viuvo = (vereador_casado / qtd_vereadores) * 100, (vereador_solteiro / qtd_vereadores) * 100, (vereador_divorciado / qtd_vereadores) * 100, (vereador_viuvo / qtd_vereadores) * 100
        porcentagens_vereador += [porcentagem_vereador_casado, porcentagem_vereador_solteiro, porcentagem_vereador_divorciado, porcentagem_vereador_viuvo]
        porcentagens_vereador += [(vereador_separado/ qtd_vereadores) * 100]

        #porcentagens total
        porcentagens= []
        porcentagem= total_candidatos
        porcentagens.append(porcentagem)
        porcentagem_LeE, porcentagem_EfI, porcentagem_EfC, porcentagem_EmI, porcentagem_EmC, porcentagem_Si, porcentagem_Sc = (LeE / total_candidatos) * 100, (EfI / total_candidatos) * 100, (EfC / total_candidatos) * 100, (EmI / total_candidatos) * 100, (EmC / total_candidatos) * 100, (Si / total_candidatos) * 100, (Sc / total_candidatos) * 100
        porcentagens+= [porcentagem_LeE, porcentagem_EfI, porcentagem_EfC, porcentagem_EmI, porcentagem_EmC, porcentagem_Si, porcentagem_Sc]
        porcentagem_genero_F, porcentagem_genero_M = (genero_F / total_candidatos) * 100, (genero_M / total_candidatos) * 100
        porcentagens+= [porcentagem_genero_F, porcentagem_genero_M]
        porcentagem_casado, porcentagem_solteiro, porcentagem_divorciado, porcentagem_viuvo = (casado / total_candidatos) * 100, (solteiro / total_candidatos) * 100, (divorciado / total_candidatos) * 100, (viuvo / total_candidatos) * 100
        porcentagens+= [porcentagem_casado, porcentagem_solteiro, porcentagem_divorciado, porcentagem_viuvo]
        porcentagens += [(separado  / total_candidatos) * 100]
        
        return porcentagens_prefeito, porcentagens_viceprefeito, porcentagens_vereador, porcentagens
       

if __name__ == '__main__':
    main = Main()
    main.grau_instrucao()
