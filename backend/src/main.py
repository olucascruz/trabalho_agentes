from fastmcp import FastMCP
from app.AgenteC1_NormaPadrao import AgenteC1_NormaPadrao
from app.AgenteC2_CompreensaoRepertorio import AgenteC2_CompreensaoRepertorio
from app.AgenteC3_Argumentacao import AgenteC3_Argumentacao
from app.AgenteC4_Coesao import AgenteC4_Coesao
from app.AgenteC5_Intervencao import AgenteC5_Intervencao

mcp = FastMCP("My MCP Server")


@mcp.tool
async def avaliar_c1(texto: str) -> dict:
    agente = AgenteC1_NormaPadrao()
    res = await agente.executar(texto)
    return {"text": res}


@mcp.tool
async def avaliar_c2(tema: str, texto: str) -> dict:
    agente = AgenteC2_CompreensaoRepertorio()
    res = await agente.executar(tema, texto)
    return {"text": res}


@mcp.tool
async def avaliar_c3(texto: str) -> dict:
    agente = AgenteC3_Argumentacao()
    res = await agente.executar(texto)
    return {"text": res}


@mcp.tool
async def avaliar_c4(texto: str) -> dict:
    agente = AgenteC4_Coesao()
    res = await agente.executar(texto)
    return {"text": res}


@mcp.tool
async def avaliar_c5(texto: str) -> dict:
    agente = AgenteC5_Intervencao()
    res = await agente.executar(texto)
    return {"text": res}


if __name__ == "__main__":
    mcp.run()
