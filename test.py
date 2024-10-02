import pandas as pd
from main import Main

import pandas as pd
from main import Main

main = Main()

def percentuals():
    total_candidatos = sum(main.faixa_etaria())
    df = pd.read_csv('consulta_cand_2024_PB.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')
    #prefeitos
    qtd_prefeitos = 0
    prefeito_LeE = prefeito_EfI = prefeito_EfC = prefeito_EmI = prefeito_EmC = prefeito_Si = prefeito_Sc = 0
    prefeito_genero_F = prefeito_genero_M = 0
    prefeito_casado = prefeito_solteiro = prefeito_divorciado = prefeito_viuvo = 0
    #vice
    qtd_vice = 0
    viceprefeito_LeE = viceprefeito_EfI = viceprefeito_EfC = viceprefeito_EmI = viceprefeito_EmC = viceprefeito_Si = viceprefeito_Sc = 0
    viceprefeito_genero_F = viceprefeito_genero_M = 0
    viceprefeito_casado = viceprefeito_solteiro = viceprefeito_divorciado = viceprefeito_viuvo = 0
    #vereadores
    qtd_vereadores = 0
    vereador_LeE = vereador_EfI = vereador_EfC = vereador_EmI = vereador_EmC = vereador_Si = vereador_Sc = 0
    vereador_genero_F = vereador_genero_M = 0
    vereador_casado = vereador_solteiro = vereador_divorciado = vereador_viuvo = 0


    for index, linha in df.iterrows():
        if linha["DS_CARGO"] == "PREFEITO":
            qtd_prefeitos += 1

            match linha["DS_GRAU_INSTRUCAO"]:
                case 'LÊ E ESCREVE':
                    prefeito_LeE += 1
                case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        prefeito_EfI += 1
                case 'ENSINO FUNDAMENTAL COMPLETO':
                    prefeito_EfC += 1
                case 'ENSINO MÉDIO INCOMPLETO':
                        prefeito_EmI += 1
                case 'ENSINO MÉDIO COMPLETO':
                    prefeito_EmC += 1
                case 'SUPERIOR INCOMPLETO':
                    prefeito_Si += 1
                case 'SUPERIOR COMPLETO':
                    prefeito_Sc += 1
            
            if linha["DS_GENERO"] == 'MASCULINO':
                prefeito_genero_M += 1

            elif linha["DS_GENERO"] == 'FEMININO':
                prefeito_genero_F += 1

            match linha["DS_ESTADO_CIVIL"]:
                case 'CASADO(A)':
                    prefeito_casado += 1
                case 'SOLTEIRO(A)':
                    prefeito_solteiro += 1
                case 'DIVORCIADO(A)':
                    prefeito_divorciado += 1
                case 'VIÚVO(A)':
                    prefeito_viuvo += 1

        elif linha["DS_CARGO"] == "VICE-PREFEITO":
            
            qtd_vice += 1
            match linha["DS_GRAU_INSTRUCAO"]:
                case 'LÊ E ESCREVE':
                    viceprefeito_LeE += 1
                case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        viceprefeito_EfI += 1
                case 'ENSINO FUNDAMENTAL COMPLETO':
                    viceprefeito_EfC += 1
                case 'ENSINO MÉDIO INCOMPLETO':
                        viceprefeito_EmI += 1
                case 'ENSINO MÉDIO COMPLETO':
                    viceprefeito_EmC += 1
                case 'SUPERIOR INCOMPLETO':
                    viceprefeito_Si += 1
                case 'SUPERIOR COMPLETO':
                    viceprefeito_Sc += 1
            
            if linha["DS_GENERO"] == 'MASCULINO':
                viceprefeito_genero_M += 1

            elif linha["DS_GENERO"] == 'FEMININO':
                viceprefeito_genero_F += 1

            match linha["DS_ESTADO_CIVIL"]:
                case 'CASADO(A)':
                    viceprefeito_casado += 1
                case 'SOLTEIRO(A)':
                    viceprefeito_solteiro += 1
                case 'DIVORCIADO(A)':
                    viceprefeito_divorciado += 1
                case 'VIÚVO(A)':
                    viceprefeito_viuvo += 1
        
        elif linha["DS_CARGO"] == "VEREADOR":
            qtd_vereadores += 1

            match linha["DS_GRAU_INSTRUCAO"]:
                case 'LÊ E ESCREVE':
                    vereador_LeE += 1
                case 'ENSINO FUNDAMENTAL INCOMPLETO':
                        vereador_EfI += 1
                case 'ENSINO FUNDAMENTAL COMPLETO':
                    vereador_EfC += 1
                case 'ENSINO MÉDIO INCOMPLETO':
                        vereador_EmI += 1
                case 'ENSINO MÉDIO COMPLETO':
                    vereador_EmC += 1
                case 'SUPERIOR INCOMPLETO':
                    vereador_Si += 1
                case 'SUPERIOR COMPLETO':
                    vereador_Sc += 1
            
            if linha["DS_GENERO"] == 'MASCULINO':
                vereador_genero_M += 1

            elif linha["DS_GENERO"] == 'FEMININO':
                vereador_genero_F += 1

            match linha["DS_ESTADO_CIVIL"]:
                case 'CASADO(A)':
                    vereador_casado += 1
                case 'SOLTEIRO(A)':
                    vereador_solteiro += 1
                case 'DIVORCIADO(A)':
                    vereador_divorciado += 1
                case 'VIÚVO(A)':
                    vereador_viuvo += 1




    #porcentagens prefeito
    porcentagens_prefeito = []
    porcentagem_prefeito = (qtd_prefeitos / total_candidatos) * 100
    print(porcentagem_prefeito)
    porcentagens_prefeito.append(porcentagem_prefeito)
    porcentagem_prefeito_LeE, porcentagem_prefeito_EfI, porcentagem_prefeito_EfC, porcentagem_prefeito_EmI, porcentagem_prefeito_EmC, porcentagem_prefeito_Si, porcentagem_prefeito_Sc = (prefeito_LeE / qtd_prefeitos) * 100, (prefeito_EfI / qtd_prefeitos) * 100, (prefeito_EfC / qtd_prefeitos) * 100, (prefeito_EmI / qtd_prefeitos) * 100, (prefeito_EmC / qtd_prefeitos) * 100, (prefeito_Si / qtd_prefeitos) * 100, (prefeito_Sc / qtd_prefeitos) * 100
    print(porcentagem_prefeito_LeE, porcentagem_prefeito_EfI, porcentagem_prefeito_EfC, porcentagem_prefeito_EmI, porcentagem_prefeito_EmC, porcentagem_prefeito_Si, porcentagem_prefeito_Sc)
    porcentagens_prefeito += [porcentagem_prefeito_LeE, porcentagem_prefeito_EfI, porcentagem_prefeito_EfC, porcentagem_prefeito_EmI, porcentagem_prefeito_EmC, porcentagem_prefeito_Si, porcentagem_prefeito_Sc]
    porcentagem_prefeito_genero_F, porcentagem_prefeito_genero_M = (prefeito_genero_F / qtd_prefeitos) * 100, (prefeito_genero_M / qtd_prefeitos) * 100
    porcentagens_prefeito += [porcentagem_prefeito_genero_F, porcentagem_prefeito_genero_M]
    porcentagem_prefeito_casado, porcentagem_prefeito_solteiro, porcentagem_prefeito_divorciado, porcentagem_prefeito_viuvo = (prefeito_casado / qtd_prefeitos) * 100, (prefeito_solteiro / qtd_prefeitos) * 100, (prefeito_divorciado / qtd_prefeitos) * 100, (prefeito_viuvo / qtd_prefeitos) * 100
    porcentagens_prefeito += [porcentagem_prefeito_casado, porcentagem_prefeito_solteiro, porcentagem_prefeito_divorciado, porcentagem_prefeito_viuvo]

    #porcentagens viceprefeito
    porcentagens_viceprefeito = []
    porcentagem_viceprefeito = (qtd_vice / total_candidatos) * 100
    print(porcentagem_viceprefeito)
    porcentagens_viceprefeito.append(porcentagem_viceprefeito)
    porcentagem_viceprefeito_LeE, porcentagem_viceprefeito_EfI, porcentagem_viceprefeito_EfC, porcentagem_viceprefeito_EmI, porcentagem_viceprefeito_EmC, porcentagem_viceprefeito_Si, porcentagem_viceprefeito_Sc = (viceprefeito_LeE / qtd_vice) * 100, (viceprefeito_EfI / qtd_vice) * 100, (viceprefeito_EfC / qtd_vice) * 100, (viceprefeito_EmI / qtd_vice) * 100, (viceprefeito_EmC / qtd_vice) * 100, (viceprefeito_Si / qtd_vice) * 100, (viceprefeito_Sc / qtd_vice) * 100
    porcentagens_viceprefeito += [porcentagem_viceprefeito_LeE, porcentagem_viceprefeito_EfI, porcentagem_viceprefeito_EfC, porcentagem_viceprefeito_EmI, porcentagem_viceprefeito_EmC, porcentagem_viceprefeito_Si, porcentagem_viceprefeito_Sc]
    porcentagem_viceprefeito_genero_F, porcentagem_viceprefeito_genero_M = (viceprefeito_genero_F / qtd_vice) * 100, (viceprefeito_genero_M / qtd_vice) * 100
    porcentagens_viceprefeito += [porcentagem_viceprefeito_genero_F, porcentagem_viceprefeito_genero_M]
    porcentagem_viceprefeito_casado, porcentagem_viceprefeito_solteiro, porcentagem_viceprefeito_divorciado, porcentagem_viceprefeito_viuvo = (viceprefeito_casado / qtd_vice) * 100, (viceprefeito_solteiro / qtd_vice) * 100, (viceprefeito_divorciado / qtd_vice) * 100, (viceprefeito_viuvo / qtd_vice) * 100
    porcentagens_viceprefeito += [porcentagem_viceprefeito_casado, porcentagem_viceprefeito_solteiro, porcentagem_viceprefeito_divorciado, porcentagem_viceprefeito_viuvo]

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
    
    return porcentagens_prefeito, porcentagens_viceprefeito, porcentagens_vereador

porcentagens_prefeito, porcentagens_viceprefeito, porcentagens_vereador = percentuals()

print()
print(porcentagens_prefeito)
print()
print(porcentagens_viceprefeito)
print()
print(porcentagens_vereador)


