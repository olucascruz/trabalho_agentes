from .AgenteBase import AgenteBase


class AgenteC1_NormaPadrao(AgenteBase):
   async def executar(self, text: str) -> str:
        return await self.pensar(
            "Avalie o texto a seguir exclusivamente quanto ao domínio da norma-padrão da língua portuguesa, sem reescrever nada. "
            "Identifique erros de gramática, ortografia, regência, pontuação e concordância, explicando cada ponto. "
            f"Em seguida, atribua uma nota de 0 a 200 conforme a Competência 1 do ENEM. Texto: {text}"
        )