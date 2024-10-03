from main import Main
import webbrowser

def generate_html_estatistica(qtd_prefeitos, qtd_vice_prefeitos, qtd_vereadores, ate21, ate40, ate60, depois60):
    main = Main()
    porcentagens_prefeito, porcentagens_viceprefeito, porcentagens_vereador, porcentagens = main.percentuals()
    lista_candidatos_por_partido = main.partido_pref()
    partidos_quantidade = ''
    for indice, linha in lista_candidatos_por_partido.iterrows():
        quantidade = linha['Quantidade']
        nomepartido = linha['NM_PARTIDO']
        corpo_html_mid = f'''
                            <tr>
                                <td>{nomepartido}</td>
                                <td>{quantidade}</td>
                            </tr>'''
        partidos_quantidade += corpo_html_mid

    html_estatistica=f'''

    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Estatísticas dos Candidatos</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body class="bg-secondary text-black">
        <div class="container">
            <header class="my-5">
                <h1 class="text-center">Estatísticas dos Candidatos</h1>
            </header>
            <main>
                <section class="mb-5"></section>
                    <h2>Quantidade de candidatos por cargo</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th style="width: 40%;">Cargo</th>
                                <th>Quantidade de candidatos</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Prefeito</td>
                                <td>{qtd_prefeitos}</td>
                            </tr>
                            <tr>
                                <td>Vice-prefeito</td>
                                <td>{qtd_vice_prefeitos}</td>
                            </tr>
                            <tr>
                                <td>Vereador</td>
                                <td>{qtd_vereadores}</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
                <section class="my-5">
                    <h2>Partidos com candidatos ao cargo de Prefeito</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>Nome do partido</th>
                                <th>Quantidade de Candidatos</th>
                            </tr>
                            </thead>
                            <tbody>
                                {partidos_quantidade}
                        </tbody>
                    </table>
                </section>
                <section class="mb-5">
                <h2>Quantidade de candidatos por faixa etária</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>Até 21 anos</th>
                                <th>Entre 22 anos e 40 anos</th>
                                <th>Entre 41 anos e 60 anos</th>
                                <th>Acima de 60 anos</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>{ate21}</td>
                                <td>{ate40}</td>
                                <td>{ate60}</td>
                                <td>{depois60}</td>
                            </tr>                        
                        </tbody>
                    </table>
                </section>
                <section class="mb-5">
                    <h2>Percentual de candidatos por cargo</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>Total {porcentagens[0]}   </th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem %</td>
                                <td>LÊ E ESCREVE {porcentagens[1]:.2f}  %</td>
                                <td>MASCULINO {porcentagens[9]:.2f}  %</td>
                                <td>CASADO(A) {porcentagens[10]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL INCOMPLETO {porcentagens[2]:.2f}  %</td>
                                <td>FEMININO {porcentagens[8]:.2f}  %</td>
                                <td>SOLTEIRO(A) {porcentagens[11]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL COMPLETO {porcentagens[3]:.2f}  %</td>
                                <td></td>
                                <td>DIVORCIADO(A) {porcentagens[12]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO INCOMPLETO {porcentagens[4]:.2f}  %</td>
                                <td></td>
                                <td>VIÚVO(A) {porcentagens[13]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO COMPLETO {porcentagens[5]:.2f}  %</td>
                                <td></td>
                                <td>SEPARADO(A) JUDICIALMENTE {porcentagens[14]:.2F} %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR INCOMPLETO {porcentagens[6]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR COMPLETO {porcentagens[7]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>                          
                        </tbody>
                    </table>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>PREFEITO {porcentagens_prefeito[0]:.2f}   %</th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem %</td>
                                <td>LÊ E ESCREVE {porcentagens_prefeito[1]:.2f}  %</td>
                                <td>MASCULINO {porcentagens_prefeito[9]:.2f}  %</td>
                                <td>CASADO(A) {porcentagens_prefeito[10]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL INCOMPLETO {porcentagens_prefeito[2]:.2f}  %</td>
                                <td>FEMININO {porcentagens_prefeito[8]:.2f}  %</td>
                                <td>SOLTEIRO(A) {porcentagens_prefeito[11]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL COMPLETO {porcentagens_prefeito[3]:.2f}  %</td>
                                <td></td>
                                <td>DIVORCIADO(A) {porcentagens_prefeito[12]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO INCOMPLETO {porcentagens_prefeito[4]:.2f}  %</td>
                                <td></td>
                                <td>VIÚVO(A) {porcentagens_prefeito[13]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO COMPLETO {porcentagens_prefeito[5]:.2f}  %</td>
                                <td></td>
                                <td>SEPARADO(A) JUDICIALMENTE {porcentagens_prefeito[14]:.2F}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR INCOMPLETO {porcentagens_prefeito[6]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR COMPLETO {porcentagens_prefeito[7]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>                             
                        </tbody>
                    </table>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>VICE-PREFEITO {porcentagens_viceprefeito[0]:.2f}   %</th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem %</td>
                                <td>LÊ E ESCREVE {porcentagens_viceprefeito[1]:.2f}  %</td>
                                <td>MASCULINO {porcentagens_viceprefeito[9]:.2f}  %</td>
                                <td>CASADO(A) {porcentagens_viceprefeito[10]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL INCOMPLETO {porcentagens_viceprefeito[2]:.2f}  %</td>
                                <td>FEMININO {porcentagens_viceprefeito[8]:.2f}  %</td>
                                <td>SOLTEIRO(A) {porcentagens_viceprefeito[11]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL COMPLETO {porcentagens_viceprefeito[3]:.2f}  %</td>
                                <td></td>
                                <td>DIVORCIADO(A) {porcentagens_viceprefeito[12]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO INCOMPLETO {porcentagens_viceprefeito[4]:.2f}  %</td>
                                <td></td>
                                <td>VIÚVO(A) {porcentagens_viceprefeito[13]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO COMPLETO {porcentagens_viceprefeito[5]:.2f}  %</td>
                                <td></td>
                                <td>SEPARADO(A) JUDICIALMENTE {porcentagens_viceprefeito[14]:.2F} %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR INCOMPLETO {porcentagens_viceprefeito[6]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR COMPLETO {porcentagens_viceprefeito[7]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>                          
                        </tbody>
                    </table>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>VEREADOR {porcentagens_vereador[0]:.2f}   %</th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem %</td>
                                <td>LÊ E ESCREVE {porcentagens_vereador[1]:.2f}  %</td>
                                <td>MASCULINO {porcentagens_vereador[9]:.2f}  %</td>
                                <td>CASADO(A) {porcentagens_vereador[10]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL INCOMPLETO {porcentagens_vereador[2]:.2f}  %</td>
                                <td>FEMININO {porcentagens_vereador[8]:.2f}  %</td>
                                <td>SOLTEIRO(A) {porcentagens_vereador[11]:.2f}  %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>ENSINO FUNDAMENTAL COMPLETO {porcentagens_vereador[3]:.2f}  %</td>
                                <td></td>
                                <td>DIVORCIADO(A) {porcentagens_vereador[12]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO INCOMPLETO {porcentagens_vereador[4]:.2f}  %</td>
                                <td></td>
                                <td>VIÚVO(A) {porcentagens_vereador[13]:.2f}  %</td>
                            </tr> 
                            <tr>
                                <td></td>
                                <td>ENSINO MÉDIO COMPLETO {porcentagens_vereador[5]:.2f}  %</td>
                                <td></td>
                                <td>SEPARADO(A) JUDICIALMENTE {porcentagens_vereador[14]:.2F} %</td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR INCOMPLETO {porcentagens_vereador[6]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>
                            <tr>
                                <td></td>
                                <td>SUPERIOR COMPLETO {porcentagens_vereador[7]:.2f}  %</td>
                                <td></td>
                                <td></td>
                            </tr>                          
                        </tbody>
                    </table>
                    
            </main>
            <footer class="text-center my-4">
                <p>&copy; 2024 TSE - Estatísticas Eleitorais.</p>
            </footer>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>t>
    </body>
    </html>

    '''
    with open('pagina_estatisticas.html', 'w', encoding='utf8') as arquivo:
        arquivo.write(html_estatistica)

    webbrowser.open('pagina_estatisticas.html')


def generate_html_candidatos(candidatos):

    for candidato in candidatos:
        candidato = candidato.split(',')
        
    html=f'''

        <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Seu Candidato</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
>
    </head>
    <body class="bg-secondary text-black">
        <div class="container">
            <header class="my-5">
                <h1 class="text-center">Candidato</h1>
            </header>
            <main>
                <div class="header-content">
                    <img src="https://raw.githubusercontent.com/davicesarmorais/fotos-candidatos-pb/refs/heads/main/fotos-candidatos-pb/FPB{candidato[4]}_div.jpg" 
                         alt="Imagem do candidato" 
                         style="width: 150px; height: auto; display: block; margin: 0 auto;">
                    <h2 class="mt-3">{candidato[2]}</h2> 
                </div>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                            
                                <th>Número do Candidato</th>
                                <th>Partido</th>
                                <th>Urna</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>{candidato[1]}</td>
                                <td>{candidato[3]}</td>
                                <td>{candidato[0]}</td>
                            </tr>
                        </tbody>
                    </table>
                </section>
            </main>
            <footer class="text-center my-4">
                <p>&copy; 2024 TSE - Estatísticas Eleitorais.</p>
            </footer>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>t>
    </body>
    </html>'''
    
    with open('pagina_candidatos.html', 'w', encoding='utf8') as arquivo:
        arquivo.write(html)

    webbrowser.open('pagina_candidatos.html')




