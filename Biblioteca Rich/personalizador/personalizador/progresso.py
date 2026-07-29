"""Módulo para exibição de conteúdos acompanhados de barras de progresso do Rich."""

import os
import time
from rich.console import Console
from rich.progress import track


def _obter_texto(texto_ou_caminho: str, is_arquivo: bool) -> str:
    if is_arquivo and os.path.exists(texto_ou_caminho):
        with open(texto_ou_caminho, "r", encoding="utf-8") as f:
            return f.read()
    return texto_ou_caminho


def exibir_progresso_simulacao(texto: str, isArquivo: bool = False) -> None:
    """Simula o carregamento do texto mostrando uma barra de progresso antes da impressão."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()

    for _ in track(range(10), description="Processando texto..."):
        time.sleep(0.1)

    console.print(f"[bold green]Texto carregado:[/bold green]\n{conteudo}")


def exibir_progresso_linhas(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto linha por linha à medida que a barra de progresso avança."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    linhas = conteudo.splitlines() or [conteudo]

    console.print("[cyan]Exibindo linhas gradualmente:[/cyan]")
    for linha in track(linhas, description="Lendo linhas..."):
        time.sleep(0.3)
        console.print(linha)