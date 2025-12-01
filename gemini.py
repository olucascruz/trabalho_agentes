import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import time

# 1. Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

# 2. Pega a chave de forma segura
api_key = os.getenv("KEY_API")
print("Usando a chave da API:", api_key)
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_response_c1(texto: str, nota: float, model):
    # 1. Montamos o Prompt para o Gemini "Professor"
    # O objetivo dele é justificar a nota que VOCÊ já definiu.
    prompt_sistema = f"""
    Você é um avaliador especialista na Competência 1 do ENEM (Norma Padrão).
    Eu tenho uma redação e a nota final dela foi: {nota} (de 0 a 200).
    
    Sua tarefa é agir como o "raciocínio" do avaliador.
    1. Analise o texto procurando erros gramaticais, de regência, crase e ortografia que justifiquem essa nota.
    2. Gere um JSON com 3 campos exatos:
       - "Question": O comando de avaliação (eu forneço o template abaixo).
       - "Complex_CoT": O pensamento passo a passo, analisando os erros e decidindo a penalidade.
       - "Response": A resposta final ao aluno, citando os erros e a nota.

    TEXTO DO ALUNO:
    "{texto}"
    
    NOTA ATRIBUÍDA: {nota}

    Gere a saída APENAS em formato JSON válido, seguindo este esquema:
    {{
        "Question": "Avalie o texto a seguir exclusivamente quanto ao domínio da norma-padrão da língua portuguesa (Competência 1 do ENEM). Texto: [inserir texto aqui]",
        "Complex_CoT": "[Seu raciocínio detalhado aqui]",
        "Response": "A nota para a Competência 1 é {nota}. O texto apresenta os seguintes desvios: [listar erros]"
    }}
    """

    # 2. Configuração para garantir JSON (Se o modelo suportar, ou via prompt)
    generation_config = {
        "response_mime_type": "application/json"
    }

    try:
        # 3. Chamada correta ao modelo
        response = model.generate_content(prompt_sistema, generation_config=generation_config)
        
        # Retorna o texto do JSON
        return response.text
        
    except Exception as e:
        print(f"Erro ao gerar: {e}")
        return None



arquivo_entrada = "essays.json"
arquivo_saida = "dataset_treino_c1.json"
novos_dados = []

# Carrega o arquivo
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    essays = json.load(f)

print(f"Total de redações: {len(essays)}")

for i, essay in enumerate(essays):
    
    # --- Trava de Segurança (3 itens) ---
    if i >= 300: 
        print("Limite de teste atingido. Parando...")
        break
    
    # 1. PEGAR O TEXTO (Está na raiz)
    texto_aluno = essay.get("texto", "")
    
    # 2. PEGAR O TEMA (Opcional, mas ajuda o modelo a entender o contexto)
    tema_redacao = essay.get("tema", "")
    
    # 3. PEGAR A NOTA (Está aninhada dentro de 'notas')
    # Primeiro pegamos o dicionário de notas, depois a Competência 1
    notas_dict = essay.get("notas", {})
    nota_c1 = notas_dict.get("Competência 1", 0.0) 

    # DICA: Se 1.0 vale 200 pontos na sua regra, você pode converter aqui:
    # nota_final = nota_c1 * 40 (Exemplo: Nível 1 = 40, Nível 5 = 200)
    # Por enquanto, vou deixar o valor original:
    
    print(f"Processando item {i+1} | Nota C1: {nota_c1}")

    try:
        # Chama o Gemini passando o texto e a nota extraída corretamente
        # (Se quiser passar o tema também, teria que alterar a função generate_response_c1 para aceitar tema)
        json_string = generate_response_c1(texto_aluno, nota_c1, model)
        
        if json_string:
            clean_str = json_string.replace("```json", "").replace("```", "").strip()
            objeto_pronto = json.loads(clean_str)
            
            # (Opcional) Adicionar o tema no dataset final para referência futura
            objeto_pronto["original_theme"] = tema_redacao
            
            novos_dados.append(objeto_pronto)
            
            with open(arquivo_saida, "w", encoding="utf-8") as f_out:
                json.dump(novos_dados, f_out, ensure_ascii=False, indent=4)
                
        time.sleep(2)

    except Exception as e:
        print(f"Erro no item {i+1}: {e}")

print("Concluído!")