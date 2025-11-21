from fastapi import FastAPI

app = FastAPI(
    title="ENEM Redaction Evaluator API",
    description="Backend para gerenciar agentes e avaliar redações.",
    version="1.0.0"
)

# Rota base
@app.get("/")
def root():
    return {"message": "API do Avaliador de Redações ENEM está rodando!"}

# Exemplo de rota para testar POST futuramente
@app.post("/avaliar")
def avaliar_redacao(redacao: str):
    # lógica dos agentes vai ficar aqui depois
    return {
        "status": "ok",
        "redacao_recebida": redacao,
        "resultado": "A avaliação será implementada em breve!"
    }
