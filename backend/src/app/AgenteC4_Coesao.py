from .AgenteBase import AgenteBase


class AgenteC4_Coesao(AgenteBase):
    async def executar(self, text: str) -> str:
         return await self.pensar(
            f"Avalie o texto exclusivamente quanto aos mecanismos de coesão textual, sem reescrever nada. "
            f"Analise o uso de conectivos, continuidade, articulação entre frases e parágrafos e progressão textual. "
            f"Depois, atribua uma nota de 0 a 200 conforme a Competência 4 do ENEM. Texto: {text}"
        )