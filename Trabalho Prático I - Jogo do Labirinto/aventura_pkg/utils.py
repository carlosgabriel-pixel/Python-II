"""
Módulo utils.
Gerencia menus, instruções, interfaces de texto com 'rich' e animações de vitória/derrota.
"""

import time
from rich.console import Console
from rich.panel import Panel

console = Console()


def imprime_menu(cor_tema: str = "cyan") -> None:
    """
    Exibe o menu principal do jogo usando formatação do painel Rich.

    Args:
        cor_tema (str): Define a cor da borda do painel exibido.
    """
    texto_menu = (
        "[1] - Jogar\n"
        "[2] - Instruções\n"
        "[3] - Assistir Resolução Recursiva (Desafio)\n"
        "[0] - Sair"
    )
    painel = Panel(
        texto_menu,
        title="[bold white]Menu Principal[/bold white]",
        border_style=cor_tema,
    )
    console.print(painel)


def imprime_instrucoes(cor_tema: str = "cyan") -> None:
    """
    Exibe as instruções e regras do jogo na tela.

    Args:
        cor_tema (str): Define a cor de destaque nas instruções.
    """
    texto = (
        "[bold yellow]Regras do Jogo:[/bold yellow]\n\n"
        "• Mova o jogador [green]@[/green] usando as teclas:\n"
        "  [bold]W[/bold] (Cima) | [bold]S[/bold] (Baixo) | [bold]A[/bold] (Esquerda) | [bold]D[/bold] (Direita)\n"
        "• Colete os itens [yellow]*[/yellow] para acumular [bold green]+10 pontos[/bold green].\n"
        "• Evite as paredes [cyan]#[/cyan] e encontre a Saída [red]S[/red] para vencer!\n"
        "• Pressione [bold]ESC[/bold] em qualquer momento durante a movimentação para sair."
    )
    console.print(Panel(texto, title="Instruções", border_style=cor_tema))


def animacao_vitoria_recursiva(passos: int = 3) -> None:
    """
    Função recursiva para disparar uma animação celebrando a vitória do jogador.

    Args:
        passos (int): Número decrescente para encerramento da animação recursiva.
    """
    if passos == 0:
        console.print(
            "[bold green]*** PARABÉNS! VOCÊ ESCAPOU DO LABIRINTO! ***[/bold green]"
        )
        return

    console.print(
        f"[bold yellow]{'★ ' * passos} VITÓRIA! {'★ ' * passos}[/bold yellow]"
    )
    time.sleep(0.5)
    animacao_vitoria_recursiva(passos - 1)


def tela_fim(vitoria: bool, pontos: int, nome: str) -> None:
    """
    Exibe a tela final da partida do jogador.

    Args:
        vitoria (bool): Sinaliza status da partida (vitória ou derrota).
        pontos (int): A pontuação final acumulada pelo jogador.
        nome (str): O nome do jogador exibido no painel final.
    """
    if vitoria:
        animacao_vitoria_recursiva(4)
        msg = f"[green]Grande trabalho, {nome}![/green]\nSua pontuação final foi: [bold yellow]{pontos}[/bold yellow] pontos!"
        console.print(Panel(msg, title="Fim de Jogo", border_style="green"))
    else:
        msg = f"[red]Não foi dessa vez, {nome}...[/red]\nSua pontuação ficou em: [yellow]{pontos}[/yellow] pontos."
        console.print(Panel(msg, title="Derrota", border_style="red"))