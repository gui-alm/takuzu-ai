# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 00:
# 00000 Nome1
# 00000 Nome2

import sys
from search import (
    Problem,
    Node,
    astar_search,
    breadth_first_tree_search,
    depth_first_tree_search,
    greedy_search,
    recursive_best_first_search,
)


class TakuzuState:
    state_id = 0

    def __init__(self, board):
        self.board = board
        self.id = TakuzuState.state_id
        TakuzuState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe


class Board:
    """Representação interna de um tabuleiro de Takuzu."""

    def __init__(self, n):
        self.size = n
        self.board = list()
        row = [2] * self.size
        for i in range(self.size):
            self.board.append(list(row))
    
    def __str__(self):
        for i in range(self.size):
            print(*self.board[i])

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO

        if(row > self.n or row < 1 or col < 1 or col > self.n):
            raise ValueError("Board: given position does not exist in the current board.")

        return self.board[row -1][col -1]

    def check_value(self, row: int, col: int, value: int):
        """Checks if the given position's value is equal to the given value"""

        return self.get_number(row, col) == value

    def set_value(self, row: int, col: int, value: int):
        """Sets the value of a certain position in the board."""

        if self.check_value(row, col, value):
            return # dont know if we need this
        if(value not in (0, 1 , 2)):
            raise ValueError("Board: values must be 0, 1 or 2.")
        self.board[row - 1][col - 1] = value

    def adjacent_vertical_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        # TODO

        if(row == 1 or row == self.n):
             # do they want it to return None or (number, None) / (None, number) ? QUESTION
            return None 

        return (self.get_number(row + 1, col), self.get_number(row + 1, col))

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO

        if(col == 1 or col == self.n):
            # do they want it to return None or (number, None) / (None, number) ? QUESTION
            return None  

        return (self.get_number(row, col - 1), self.get_number(row, col + 1))

    @staticmethod
    def parse_instance_from_stdin():
        """Lê o test do standard input (stdin) que é passado como argumento
        e retorna uma instância da classe Board.

        Por exemplo:
            $ python3 takuzu.py < input_T01

            > from sys import stdin
            > stdin.readline()
        """
        # TODO
        pass

    # TODO: outros metodos da classe


class Takuzu(Problem):
    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        pass

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO
        pass

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO
        pass

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        # TODO
        pass

    def h(self, node: Node):
        """Função heuristica utilizada para a procura A*."""
        # TODO
        pass

    # TODO: outros metodos da classe


if __name__ == "__main__":
    # TODO:
    # Ler o ficheiro do standard input,
    # Usar uma técnica de procura para resolver a instância,
    # Retirar a solução a partir do nó resultante,
    # Imprimir para o standard output no formato indicado.
    pass
