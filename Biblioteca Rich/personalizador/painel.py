"""Módulo para exibição de conteúdos dentro de painéis estilizados do Rich."""

import os
from rich.console import Console
from rich.panel import Panel


def _obter_texto(texto_ou_caminho: str, is_arquivo: bool) -> str:
    if is_arquivo and os.path.exists(texto_ou_caminho):
        with open(texto_ou_caminho, "r", encoding="utf-8") as f:
            return f.read()
    return texto_ou_caminho


def exibir_painel_simples(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto em um painel simples com bordas azuis."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    painel = Panel(conteudo, title="Painel Simples", border_style="blue")
    console.print(painel)


def exibir_painel_alerta(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto em um painel estilo alerta com bordas vermelhas e título destacado."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    painel = Panel(f"[bold red]{conteudo}[/bold red]", title="⚠️ ALERTA ⚠️", border_style="red")
    console.print(painel)