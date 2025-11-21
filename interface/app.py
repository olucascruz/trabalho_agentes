import streamlit as st
from pypdf import PdfReader

# ----------------------------------------------------
# FUNÇÃO AUXILIAR – ler PDF
# ----------------------------------------------------
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except:
        return None

# ----------------------------------------------------
# INTERFACE
# ----------------------------------------------------
st.set_page_config(page_title="Avaliador de Redação ENEM", layout="centered")

st.title("📄 Avaliador de Redação do ENEM – MVP")
st.write("Avalie sua redação automaticamente usando IA e critérios oficiais do ENEM.")

# ----------------------------------------------------
# Entrada da redação
# ----------------------------------------------------
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

# ----------------------------------------------------
# Tema
# ----------------------------------------------------
st.subheader("2️⃣ Informe o tema (opcional)")
tema = st.text_input("Tema da redação:")

# ----------------------------------------------------
# Botão de avaliação
# ----------------------------------------------------
st.subheader("3️⃣ Avaliação")
avaliar = st.button("🚀 Avaliar Redação")

# ----------------------------------------------------
# Resultado (placeholder)
# ----------------------------------------------------
if avaliar:
    if not redacao_texto.strip():
        st.error("Por favor, insira ou envie sua redação antes de avaliar.")
    else:
        # Aqui você irá chamar seus agentes de IA
        st.info("🔍 Avaliando redação... (mock)")

        # MOCK – Você depois substitui por chamadas reais
        competencias = {
            "Competência 1 — Norma Culta": "160/200\nUso adequado da norma culta, mas com alguns desvios.",
            "Competência 2 — Compreensão do Tema": "180/200\nBoa abordagem do tema e desenvolvimento consistente.",
            "Competência 3 — Organização Argumentativa": "160/200\nArgumentos relevantes, porém pouco aprofundados.",
            "Competência 4 — Coesão e Estruturação": "200/200\nExcelentes conectores e progressão de ideias.",
            "Competência 5 — Proposta de Intervenção": "120/200\nProposta incompleta, faltam atores e detalhamento."
        }

        st.subheader("📊 Resultado da Avaliação")

        for comp, resultado in competencias.items():
            with st.expander(comp):
                st.write(resultado)

        st.success("Avaliação concluída! (resultado simulado)")   
