"""
Módulo labirinto.
Gerencia a criação e exibição do labirinto do jogo.
"""

import random
from rich.console import Console

console = Console()


def criar_labirinto(largura: int = 15, altura: int = 10) -> list:
    """
    Gera um labirinto bidimensional com paredes, corredor, itens e saída.

    Args:
        largura (int): A largura (colunas) do labirinto.
        altura (int): A altura (linhas) do labirinto.

    Returns:
        list: Matriz contendo o mapa gerado.
    """
    matriz = [[" " for _ in range(largura)] for _ in range(altura)]

    for linha in range(altura):
        for col in range(largura):
            # Paredes nas bordas
            if linha == 0 or linha == altura - 1 or col == 0 or col == largura - 1:
                matriz[linha][col] = "#"
            # Obstáculos aleatórios pelo mapa
            elif random.random() < 0.2:
                matriz[linha][col] = "#"

    # Define itens colecionáveis ('*') espalhados no labirinto
    for _ in range((largura * altura) // 15):
        lx = random.randint(1, altura - 2)
        ly = random.randint(1, largura - 2)
        matriz[lx][ly] = "*"

    # Posição livre inicial do jogador e a saída do labirinto
    matriz[1][1] = " "
    matriz[altura - 2][largura - 2] = "S"
    return matriz


def imprimir_labirinto(
    labirinto: list, jogador_pos: tuple, cor_tema: str = "cyan"
) -> None:
    """
    Imprime visualmente o labirinto usando a biblioteca Rich.

    Args:
        labirinto (list): Matriz atual do labirinto.
        jogador_pos (tuple): Coordenadas atual (linha, coluna) do jogador.
        cor_tema (str): Cor principal usada na exibição.
    """
    for linha_idx, linha in enumerate(labirinto):
        linha_str = ""
        for col_idx, celula in enumerate(linha):
            if (linha_idx, col_idx) == jogador_pos:
                linha_str += "[bold green]@[/bold green]"
            elif celula == "#":
                linha_str += f"[bold {cor_tema}]#[/bold {cor_tema}]"
            elif celula == "*":
                linha_str += "[yellow]*[/yellow]"
            elif celula == "S":
                linha_str += "[bold red]S[/bold red]"
            else:
                linha_str += " "
        console.print(linha_str)