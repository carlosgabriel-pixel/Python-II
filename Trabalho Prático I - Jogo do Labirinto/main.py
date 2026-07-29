"""
Módulo Principal - Execução do Aventura no Labirinto.
Gerencia a CLI através de argumentos, execução do laço principal do jogo e menus.
"""

import argparse
import time
from rich.console import Console
from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover, resolver_recursivo
from aventura_pkg.utils import imprime_menu, imprime_instrucoes, tela_fim

console = Console()


def configurar_cli() -> argparse.Namespace:
    """
    Configura e lê os parâmetros via linha de comando para a execução.

    Returns:
        argparse.Namespace: Objeto preenchido com argumentos acionados pelo usuário.
    """
    parser = argparse.ArgumentParser(
        description="Aventura no Labirinto - Um jogo modular via terminal."
    )
    # 5 Parâmetros, contendo uma obrigatoriedade (--name)
    parser.add_argument(
        "--name", required=True, help="Nome do(a) jogador(a) [Obrigatório]"
    )
    parser.add_argument(
        "--color",
        default="cyan",
        choices=["cyan", "red", "green", "blue", "magenta"],
        help="Cor de destaque principal no terminal",
    )
    parser.add_argument(
        "--dificuldade",
        type=int,
        default=1,
        choices=[1, 2, 3],
        help="Níveis do labirinto (1: Pequeno, 2: Médio, 3: Grande)",
    )
    parser.add_argument(
        "--disable-sound",
        action="store_true",
        help="Desativa o som durante o jogo (opcional)",
    )
    parser.add_argument(
        "--max-steps",
        type=int,
        default=100,
        help="Máximo de passos permitidos no labirinto",
    )

    return parser.parse_args()


def jogar(args: argparse.Namespace) -> None:
    """
    Loop de execução principal da partida do jogador.
    """
    tamanhos = {1: (10, 8), 2: (15, 10), 3: (20, 12)}
    largura, altura = tamanhos[args.dificuldade]

    labirinto = criar_labirinto(largura, altura)
    jogador = iniciar_jogador()
    passos_restantes = args.max-steps if hasattr(args, "max_steps") else 100

    while passos_restantes > 0:
        console.clear()
        console.print(
            f"[bold {args.color}]--- AVENTURA NO LABIRINTO ---[/bold {args.color}]"
        )
        console.print(
            f"Jogador: [bold]{args.name}[/bold] | Pontos: [bold yellow]{jogador['pontos']}[/bold yellow] | Passos: [bold]{passos_restantes}[/bold]"
        )

        imprimir_labirinto(labirinto, jogador["pos"], args.color)

        l_pos, c_pos = jogador["pos"]
        # Verifica condição de vitória na saída ('S')
        if labirinto[l_pos][c_pos] == "S":
            console.clear()
            tela_fim(vitoria=True, pontos=jogador["pontos"], nome=args.name)
            return

        if not mover(jogador, labirinto):
            break

        passos_restantes -= 1

    # Condição caso encerrem os movimentos ou o usuário saia com o 'ESC'
    console.clear()
    tela_fim(vitoria=False, pontos=jogador["pontos"], nome=args.name)


def exibir_resolucao_recursiva(args: argparse.Namespace) -> None:
    """
    Resolve automaticamente um labirinto e exibe visualmente para o jogador.
    """
    labirinto = criar_labirinto(10, 8)
    # Garante mapa sem bloqueios para testar a rota em segurança
    caminho = resolver_recursivo(labirinto, (1, 1), (6, 8))

    if not caminho:
        console.print(
            "[bold red]Não existe caminho possível neste mapa de testes![/bold red]"
        )
        return

    for pos in caminho:
        console.clear()
        console.print(
            "[bold yellow]Assistindo Resolução Recursiva...[/bold yellow]"
        )
        imprimir_labirinto(labirinto, pos, args.color)
        time.sleep(0.3)


def main() -> None:
    """
    Início do sistema e controle de transições do Menu via `match-case`.
    """
    args = configurar_cli()

    while True:
        console.print(f"\n[bold]Bem-vindo(a), {args.name}![/bold]")
        imprime_menu(args.color)
        opcao = input("Escolha uma opção: ").strip()

        # Estrutura match-case obrigatória implementada nas opções
        match opcao:
            case "1":
                jogar(args)
            case "2":
                imprime_instrucoes(args.color)
            case "3":
                exibir_resolucao_recursiva(args)
            case "0":
                console.print(
                    "[bold yellow]Obrigado por jogar! Até a próxima.[/bold yellow]"
                )
                break
            case _:
                console.print(
                    "[bold red]Opção inválida! Escolha um número válido do menu.[/bold red]"
                )


if __name__ == "__main__":
    main()