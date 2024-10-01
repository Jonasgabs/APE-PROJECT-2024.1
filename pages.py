from main import Main

def generate_html_estatistica(qtd_prefeitos, qtd_vice_prefeitos, qtd_vereadores, ate21, ate40, ate60, depois60):
    html_estatistica_top=f'''

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
                </section>'''

    lista_candidatos_por_partido = Main.partido_pref()
    html_estatistica_mid_fixa = f'''

                <section class="my-5">
                    <h2>Partidos com candidatos ao cargo de Prefeito</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th>Nome do partido</th>
                                <th>Quantidade de Candidatos</th>
                            </tr>
                            </thead>'''

                            '''
                        <tbody>
                            <tr>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                            </tr>
                        </tbody>
                    </table>
                </section>
                <section class="mb-5">'''

    html_estatistica_down = f'''

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
                                <th></th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem</td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
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
   


def generate_html_candidatos(candidatos):
    html=f'''

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
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                            </tr>
                            <tr>
                                <td>Vice-prefeito</td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                            </tr>
                            <tr>
                                <td>Vereador</td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
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
                            <tr>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                            </tr>
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
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                            </tr>                        
                        </tbody>
                    </table>
                </section>
                <section class="mb-5">
                    <h2>Percentual de candidatos por cargo</h2>
                    <table class="table table-dark table-hover">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Grau de instrução</th>
                                <th>Gênero</th>
                                <th>Estado Civil</th>
                            </tr>
                            </thead>
                        <tbody>
                            <tr>
                                <td>Porcentagem</td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
                                <td>variavel <!-- inserir a variavel correspondente--></td>
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
    return html


def getdata(candidatos):
    print(candidatos)
    
#getdata(municipio, cargo)

#ver como utilizar no app.py
'''
def abrir_html(municipio, cargo):
    
    arquivo_html = 'pagina_candidato.html'  
    webbrowser.open_new_tab(arquivo_html)
'''
