# import nltk
# nltk.download('punkt_tab')
import json
import uol_redacoes_xml


essays = uol_redacoes_xml.load()
print(len(essays))
# ~2000

qnt_essays = len(essays)


import json
import os

def add_essay_in_json(essay, filename="essays.json"):
    # Extrai o tema (primeira linha do prompt)
    tema = str(essay.prompt).split("\n")[0].strip()

    # Cria o dicionário final
    item = {
        "tema": tema,
        "texto": essay.text,
        "notas": essay.criteria_scores
    }

    # Se o arquivo existir, carrega. Senão, começa com lista vazia.
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Adiciona nova redação
    data.append(item)

    # Salva tudo novamente
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

        


for essay in essays:
    add_essay_in_json(essay)



# texto original da primeira redação
print([attr for attr in essays[0].__dir__() if not attr.startswith('_')])
# exibe os atributos do objeto de redação (exceto os privados, que começam com '_')