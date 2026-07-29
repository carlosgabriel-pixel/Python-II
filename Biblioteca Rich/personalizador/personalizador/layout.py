"""Módulo para exibição de conteúdos com layouts do Rich."""

import os
from rich.console import Console
from rich.layout import Layout


def _obter_texto(texto_ou_caminho: str, is_arquivo: bool) -> str:
    """Função auxiliar para ler o texto direto ou do arquivo."""
    if is_arquivo and os.path.exists(texto_ou_caminho):
        with open(texto_ou_caminho, "r", encoding="utf-8") as f:
            return f.read()
    return texto_ou_caminho


def exibir_layout_divivido(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto em um layout dividido verticalmente em duas seções."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    layout = Layout()

    layout.split_column(
        Layout(name="topo", size=3),
        Layout(name="principal")
    )
    layout["topo"].update("[bold blue]=== VISUALIZAÇÃO DE LAYOUT ===")    layout["principal"].update(conteudo)

    console.print(layout)


def exibir_layout_grade(texto: str, isArquivo: bool = False) -> None:
    """Exibe o texto duplicado lado a lado em um layout horizontal."""
    conteudo = _obter_texto(texto, isArquivo)
    console = Console()
    layout = Layout()

    layout.split_row(
        Layout(name="esquerda"),
        Layout(name="direita")
    )
    layout["esquerda"].update(f"[green]Painel Esquerdo:[/green]\n{conteudo}")
    layout["direita"].update(f"[yellow]Painel Direito:[/yellow]\n{conteudo}")

    console.print(layout)