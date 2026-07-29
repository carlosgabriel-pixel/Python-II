"""Módulo para exibição de conteúdos com estilos de texto avançados do Rich."""

import os
from rich.console import Console
from rich.text import Text


def _obter_texto(texto_ou_caminho: str, is_arquivo: bool) -> str:
    if is_arquivo and os.path.exists(texto_ou_caminho):
        with open(texto_ou_caminho, "r", encoding="utf-8") as f:
            return f.read()
    return texto_ou_caminho


def exibir_texto_destacado(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto estilizado com formatação negrito, sublinhado e cor magenta."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    txt = Text(conteudo, style="bold underline magenta")
    console.print(txt)


def exibir_texto_arco_iris(texto: str, isArquivo: bool = False) -> None:
    """Exibe cada caractere do texto alternando entre cores para um efeito colorido."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    cores = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    txt = Text()

    for i, char in enumerate(conteudo):
        cor = cores[i % len(cores)]
        txt.append(char, style=f"bold {cor}")

    console.print(txt)