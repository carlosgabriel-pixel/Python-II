"""
Módulo jogador.
Controla os movimentos, pontuação e soluções recursivas para o jogador.
"""

from pynput import keyboard


def iniciar_jogador() -> dict:
    """
    Inicializa o estado base do jogador no início do jogo.

    Returns:
        dict: Dicionário contendo a posição e pontuação atual.
    """
    return {"pos": (1, 1), "pontos": 0}


def pontuar(jogador: dict, valor: int = 10) -> int:
    """
    Atualiza a pontuação do jogador.

    Args:
        jogador (dict): Dicionário com os dados do jogador.
        valor (int): Pontos a somar na pontuação atual.

    Returns:
        int: Nova pontuação do jogador.
    """
    jogador["pontos"] += valor
    return jogador["pontos"]


def mover(jogador: dict, labirinto: list) -> bool:
    """
    Lê a tecla pressionada via `pynput` e movimenta o jogador se não houver colisão.

    Args:
        jogador (dict): Dicionário com posição e dados do jogador.
        labirinto (list): Matriz representando o labirinto.

    Returns:
        bool: Retorna True em movimentos válidos, False caso finalize ou falhe.
    """
    pos_atual = jogador["pos"]
    nova_pos = pos_atual

    def on_press(key):
        nonlocal nova_pos
        try:
            char = key.char.lower()
            l, c = pos_atual
            if char == "w":
                nova_pos = (l - 1, c)
            elif char == "s":
                nova_pos = (l + 1, c)
            elif char == "a":
                nova_pos = (l, c - 1)
            elif char == "d":
                nova_pos = (l, c + 1)
        except AttributeError:
            if key == keyboard.Key.esc:
                nova_pos = None
        return False  # Para a escuta de teclado após uma tecla

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    if nova_pos is None:
        return False

    l_nova, c_nova = nova_pos
    # Verifica se há colisões nas paredes
    if labirinto[l_nova][c_nova] != "#":
        jogador["pos"] = nova_pos
        if labirinto[l_nova][c_nova] == "*":
            pontuar(jogador, 10)
            labirinto[l_nova][c_nova] = " "
        return True
    return False


def resolver_recursivo(
    labirinto: list, atual: tuple, fim: tuple, visitados: set = None
) -> list:
    """
    Função recursiva para encontrar o caminho para solucionar o labirinto via Backtracking.

    Args:
        labirinto (list): A matriz do labirinto.
        atual (tuple): As coordenadas da posição investigada atualmente.
        fim (tuple): As coordenadas do objetivo/saída.
        visitados (set, opcional): Registro dos locais percorrido.

    Returns:
        list: Lista sequencial contendo as coordenadas do caminho da vitória ou lista vazia.
    """
    if visitados is None:
        visitados = set()

    # Caso Base 1: Alcançou o objetivo
    if atual == fim:
        return [atual]

    l, c = atual
    # Caso Base 2: Posição fora do limite, parede ou já visitada
    if (
        l < 0
        or l >= len(labirinto)
        or c < 0
        or c >= len(labirinto[0])
        or labirinto[l][c] == "#"
        or atual in visitados
    ):
        return []

    visitados.add(atual)

    # Passos Recursivos nas 4 direções
    direcoes = [(l - 1, c), (l + 1, c), (l, c - 1), (l, c + 1)]
    for prox in direcoes:
        caminho = resolver_recursivo(labirinto, prox, fim, visitados)
        if caminho:
            return [atual] + caminho

    return []