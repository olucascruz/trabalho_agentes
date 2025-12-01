import streamlit as st
from pypdf import PdfReader
import asyncio
from fastmcp import Client



# FUNÇÃO AUXILIAR – ler PDF
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except:
        return None


# INTERFACE
st.set_page_config(page_title="Avaliador de Redação ENEM", layout="centered")

st.title("📄 Avaliador de Redação do ENEM – MVP")
st.write("Avalie sua redação automaticamente usando IA e critérios oficiais do ENEM.")

# Entrada da redação
st.subheader("1️⃣ Envie sua redação")
input_type = st.radio(
    "Selecione o formato da entrada:",
    ["Digite o texto", "Enviar PDF"],
    horizontal=True
)

redacao_texto = ""

if input_type == "Digite o texto":
    redacao_texto = st.text_area(
        "Cole sua redação aqui:",
        height=250,
        placeholder="Digite sua redação do ENEM aqui..."
    )
else:
    uploaded_pdf = st.file_uploader("Envie o PDF da sua redação", type=["pdf"])
    if uploaded_pdf:
        redacao_texto = extract_text_from_pdf(uploaded_pdf)
        if redacao_texto:
            st.success("PDF lido com sucesso!")
            st.text_area("Texto extraído:", redacao_texto, height=250)
        else:
            st.error("Não foi possível ler o PDF.")

# Tema
st.subheader("2️⃣ Informe o tema (opcional)")
tema = st.text_input("Tema da redação:")


# Botão de avaliação
st.subheader("3️⃣ Avaliação")
avaliar = st.button("🚀 Avaliar Redação")

# Resultado
if avaliar:
    if not redacao_texto.strip():
        st.error("Por favor, insira ou envie sua redação antes de avaliar.")
    else:
        server_path = r"C:\Users\Lucas\Desktop\trabalho_agentes\backend\src\main.py"

        st.subheader("📊 Resultado da Avaliação (em tempo real)")

        # Criar placeholders individuais
        placeholders = {
            "avaliar_c1": st.empty(),
            "avaliar_c2": st.empty(),
            "avaliar_c3": st.empty(),
            "avaliar_c4": st.empty(),
            "avaliar_c5": st.empty(),
        }

        # Nomes bonitos p/ interface
        nomes = {
            "avaliar_c1": "Competência 1 — Norma Culta",
            "avaliar_c2": "Competência 2 — Compreensão do Tema",
            "avaliar_c3": "Competência 3 — Organização Argumentativa",
            "avaliar_c4": "Competência 4 — Coesão e Estruturação",
            "avaliar_c5": "Competência 5 — Proposta de Intervenção",
        }

        async def run_async():
            async with Client(server_path) as client:

                chamadas = [
                    ("avaliar_c1", {"texto": redacao_texto}),
                    ("avaliar_c2", {"tema": tema, "texto": redacao_texto}),
                    ("avaliar_c3", {"texto": redacao_texto}),
                    ("avaliar_c4", {"texto": redacao_texto}),
                    ("avaliar_c5", {"texto": redacao_texto}),
                ]

                # 🔥 EXECUÇÃO SEQUENCIAL — UM POR VEZ
                for tool_name, payload in chamadas:
                    try:
                        result = await client.call_tool(tool_name, payload)

                        # SEMPRE é CallToolResult → pega texto diretamente
                        try:
                            texto_final = result.content[0].text["text"]
                        except:
                            texto_final = str(result)  # fallback de segurança

                        placeholders[tool_name].info(
                            f"🔎 **{nomes[tool_name]}**\n\n{texto_final}"
                        )

                    except Exception as e:
                        placeholders[tool_name].error(
                            f"Erro na ferramenta {tool_name}: {e}"
                        )

            st.success("✔️ Todas as avaliações foram concluídas!")

        # Executar async (com fallback para loop já existente)
        try:
            asyncio.run(run_async())
        except RuntimeError:
            loop = asyncio.new_event_loop()
            try:
                asyncio.set_event_loop(loop)
                loop.run_until_complete(run_async())
            finally:
                asyncio.set_event_loop(None)
                loop.close()
