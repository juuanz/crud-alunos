import json

def carregar_alunos():
    try:
        with open('alunos.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_alunos(alunos):
    with open ('alunos.json','w') as f:
        json.dump(alunos,f)
