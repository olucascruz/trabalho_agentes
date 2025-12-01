from .AgenteBase import AgenteBase


class AgenteC5_Intervencao(AgenteBase):
    async def executar(self, text: str) -> str:
         return await self.pensar(
            f"Avalie o texto exclusivamente quanto à proposta de intervenção, sem reescrever nada. "
            f"Verifique se apresenta ação, agente, modo/meio, finalidade e detalhamento, respeitando os direitos humanos. "
            f"Depois, atribua uma nota de 0 a 200 conforme a Competência 5 do ENEM. Texto: {text}"
        )