from .AgenteBase import AgenteBase


class AgenteC2_CompreensaoRepertorio(AgenteBase):
    async def executar(self, text: str, tema:str) -> str:
        return await self.pensar(
            f"Avalie o texto exclusivamente quanto à compreensão do tema :{tema}, desenvolvimento das ideias e uso de repertório sociocultural, "
            f"sem reescrever nada. Verifique se o texto aborda o tema, se possui argumentos pertinentes e se o repertório é válido. "
            f"Depois, atribua uma nota de 0 a 200 conforme a Competência 2 do ENEM. Texto: {text}"
        )