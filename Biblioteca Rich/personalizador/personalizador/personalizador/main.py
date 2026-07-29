"""Interface de Linha de Comando (CLI) para acessar os módulos do personalizador."""

import argparse
import sys
from personalizador import layout, painel, progresso, estilo

MODULOS = {
    "1": ("layout", layout),
    "layout": ("layout", layout),
    "2": ("painel", painel),
    "painel": ("painel", painel),
    "3": ("progresso", progresso),
    "progresso": ("progresso", progresso),
    "4": ("estilo", estilo),
    "estilo": ("estilo", estilo)
}

FUNCOES = {
    "layout": {
        "1": ("exibir_layout_divivido", layout.exibir_layout_divivido),
        "exibir_layout_divivido": ("exibir_layout_divivido", layout.exibir_layout_divivido),
        "2": ("exibir_layout_grade", layout.exibir_layout_grade),
        "exibir_layout_grade": ("exibir_layout_grade", layout.exibir_layout_grade),
    },
    "painel": {
        "1": ("exibir_painel_simples", painel.exibir_painel_simples),
        "exibir_painel_simples": ("exibir_painel_simples", painel.exibir_painel_simples),
        "2": ("exibir_painel_alerta", painel.exibir_painel_alerta),
        "exibir_painel_alerta": ("exibir_painel_alerta", painel.exibir_painel_alerta),
    },
    "progresso": {
        "1": ("exibir_progresso_simulacao", progresso.exibir_progresso_simulacao),
        "exibir_progresso_simulacao": ("exibir_progresso_simulacao", progresso.exibir_progresso_simulacao),
        "2": ("exibir_progresso_linhas", progresso.exibir_progresso_linhas),
        "exibir_progresso_linhas": ("exibir_progresso_linhas", progresso.exibir_progresso_linhas),
    },
    "estilo": {
        "1": ("exibir_texto_destacado", estilo.exibir_texto_destacado),
        "exibir_texto_destacado": ("exibir_texto_destacado", estilo.exibir_texto_destacado),
        "2": ("exibir_texto_arco_iris", estilo.exibir_texto_arco_iris),
        "exibir_texto_arco_iris": ("exibir_texto_arco_iris", estilo.exibir_texto_arco_iris),
    }
}


def main():
    parser = argparse.ArgumentParser(
        description="CLI para personalização de texto utilizando a biblioteca Rich."
    )

    parser.add_argument(
        "texto",
        type=str,
        help="Texto simples ou caminho para um arquivo de texto a ser formatado."
    )

    parser.add_argument(
        "-a", "--arquivo",
        action="store_true",
        help="Ative este flag caso o argumento positional seja o caminho para um arquivo."
    )

    parser.add_argument(
        "-m", "--modulo",
        type=str,
        default="painel",
        help="Escolha o módulo a acessar. Opções disponíveis: 1 ou layout, 2 ou painel, 3 ou progresso, 4 ou estilo (Padrão: painel)."
    )

    parser.add_argument(
        "-f", "--funcao",
        type=str,
        default="1",
        help="Escolha a função a acessar dentro do módulo selecionado. "
             "Layout: [1 ou exibir_layout_divivido, 2 ou exibir_layout_grade]. "
             "Painel: [1 ou exibir_painel_simples, 2 ou exibir_painel_alerta]. "
             "Progresso: [1 ou exibir_progresso_simulacao, 2 ou exibir_progresso_linhas]. "
             "Estilo: [1 ou exibir_texto_destacado, 2 ou exibir_texto_arco_iris]. (Padrão: 1)."
    )

    args = parser.parse_args()

    mod_key = args.modulo.lower()
    if mod_key not in MODULOS:
        print(f"Erro: Módulo '{args.modulo}' inválido. Veja as opções com --help.", file=sys.stderr)
        sys.exit(1)

    nome_modulo, _ = MODULOS[mod_key]

    func_key = args.funcao.lower()
    if func_key not in FUNCOES[nome_modulo]:
        print(f"Erro: Função '{args.funcao}' inválida para o módulo '{nome_modulo}'. Veja as opções com --help.", file=sys.stderr)
        sys.exit(1)

    _, func_exec = FUNCOES[nome_modulo][func_key]

    # Executa a função escolhida
    func_exec(args.texto, isArquivo=args.arquivo)


if __name__ == "__main__":
    main()
    