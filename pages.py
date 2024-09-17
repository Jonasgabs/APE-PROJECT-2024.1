from main import Main
from app import window2

'''def pages_style():
    cadidate_template_head = f'''




'''


    cadidate_template_footer = f'''



'''

 
    # Dados a serem inseridos no template
    data = {
        'candidato': 'acessar estas variáveis pelo preenchido pelo usuário do app.py (verificar com o gabriel)',
        'heading': 'xxxxxxxx',

    }

    # Preenchendo o template com os dados

    html_content_head = cadidate_template_head.format(
        title=data['title'],
        heading=data['heading'], ### tem que escoler ainda os nomes que vai botar 
        message=data['message']
    )

    html_content_footer = cadidate_template_footer.format(
        title=data['title'],
        heading=data['heading'], ### tem que escolher ainda os nomes que vai botar 
        message=data['message']
    )


    # Nome do arquivo HTML de saída
    output_file = 'pagina_candidato.html'

    # Escrevendo o conteúdo HTML no arquivo
    with open(output_file, 'w') as file:
        file.write(html_content_head, html_content_footer)'''

#cargo, municipio = app.window()


def getdata(municipio, cargo):
    window2()
   
    main = Main()
    candidatos = main.municipios_cargos(municipio, cargo)
    print(candidatos)
    
#getdata(municipio, cargo)

''' ver como utilizar no app.py

def abrir_html(municipio, cargo):
    
    arquivo_html = 'pagina_candidato.html'  
    webbrowser.open_new_tab(arquivo_html)
'''