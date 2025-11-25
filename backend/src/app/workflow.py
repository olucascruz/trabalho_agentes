from AgenteC1_NormaPadrao import AgenteC1_NormaPadrao
from AgenteC2_CompreensaoRepertorio import AgenteC2_CompreensaoRepertorio
from AgenteC3_Argumentacao import AgenteC3_Argumentacao
from AgenteC4_Coesao import AgenteC4_Coesao
from AgenteC5_Intervencao import AgenteC5_Intervencao


import asyncio
import time
from colorama import Fore, Style, init

init(autoreset=True)


# ==========================
# 🧠 Sistema de agentes
# ==========================
class SistemaAgentes:
    def __init__(self, tema: str, texto: str):
        self.tema = tema
        self.texto = texto

        self.agente_c1 = AgenteC1_NormaPadrao()
        self.agente_c2 = AgenteC2_CompreensaoRepertorio()
        self.agente_c3 = AgenteC3_Argumentacao()
        self.agente_c4 = AgenteC4_Coesao()  
        self.agente_c5 = AgenteC5_Intervencao()

    async def executar_fluxo(self):
        inicio_total = time.time()

        tarefas = [
            self.agente_c1.executar(self.texto),
            self.agente_c2.executar(self.tema, self.texto),
            self.agente_c3.executar(self.texto),
            self.agente_c4.executar(self.texto),
            self.agente_c5.executar(self.texto),
        ]

        resultados = await asyncio.gather(*tarefas)


        print("\n🔍 Resultados por competência:\n" + "-"*60)
        for i, r in enumerate(resultados, 1):
            print(f"\n📌 Competência {i}:\n{r}\n")

        fim_total = time.time()
        print(f"\n⏱️ Tempo total: {fim_total - inicio_total:.2f} segundos\n")

        return resultados


# ==========================
# 🚀 Execução principal
# ==========================
if __name__ == "__main__":
    tema = "Os desafios da preservação ambiental no Brasil contemporâneo"
    texto = """A preservação ambiental no Brasil contemporâneo apresenta-se como um dos maiores desafios para o desenvolvimento sustentável. Embora o país seja reconhecido mundialmente por sua extensa biodiversidade, problemas como desmatamento, poluição e uso inadequado dos recursos naturais continuam crescendo de forma preocupante. Nesse contexto, torna-se essencial compreender as causas desse cenário e propor soluções que incentivem uma mudança efetiva.

Primeiramente, observa-se que a falta de fiscalização eficiente está entre os principais fatores que agravam a degradação ambiental. Muitas regiões, como a Amazônia, sofrem com atividades ilegais de extração de madeira e garimpo, impulsionadas pela ausência do Estado e pelo interesse econômico de grupos organizados. Essa falha institucional dificulta a proteção dos ecossistemas e contribui para o aumento das emissões de gases poluentes, afetando o equilíbrio climático global.

Além disso, a baixa conscientização da população também é um obstáculo relevante. Grande parte dos cidadãos ainda não compreende a importância de práticas sustentáveis, como reciclagem e consumo responsável. Essa falta de engajamento social é reforçada por campanhas educativas insuficientes e por um sistema escolar que nem sempre prioriza a educação ambiental. Dessa forma, atitudes individuais que poderiam mitigar impactos ambientais acabam sendo negligenciadas.

Diante desse cenário, é imprescindível que o poder público invista em políticas mais rigorosas de proteção ambiental, aliadas à fiscalização tecnológica e integrada entre órgãos competentes. Paralelamente, campanhas educativas contínuas devem ser promovidas, estimulando a formação de cidadãos conscientes de seu papel na preservação do meio ambiente. Portanto, somente com ações conjuntas, envolvendo governo e sociedade, será possível superar os desafios atuais e garantir um futuro sustentável para as próximas gerações."""

    sistema = SistemaAgentes(tema=tema, texto=texto)

    asyncio.run(sistema.executar_fluxo())