from AgenteBase import AgenteBase


class AgenteC3_Argumentacao(AgenteBase):
    async def executar(self, text: str) -> str:
        return await self.pensar(
        f"Avalie o texto exclusivamente quanto à capacidade de argumentação, organização lógica das ideias e construção da defesa de um ponto de vista, "
        f"sem reescrever nada. Analise a clareza, a progressão e a lógica interna dos argumentos. "
        f"Depois, atribua uma nota de 0 a 200 conforme a Competência 3 do ENEM. Texto: {text}"
    )