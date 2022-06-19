# takuzu.py: Template para implementação do projeto de Inteligência Artificial 2021/2022.
# Devem alterar as classes e funções neste ficheiro de acordo com as instruções do enunciado.
# Além das funções e classes já definidas, podem acrescentar outras que considerem pertinentes.

# Grupo 6:
# 99230 Guilherme Almeida Patrão
# 99248 Joao Domingos Baracho

from os import stat
import sys
import numpy as np
from regex import R
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
        self.board_size = board.get_size()
        TakuzuState.state_id += 1

    def __lt__(self, other):
        return self.id < other.id

    # TODO: outros metodos da classe

    def get_board(self):
        return self.board.get_board()

    def valid_action(self, row, col, piece):
        row_c = self.board.get_row(row)
        row_c[col] = piece
        if not valid(row_c):
            return False

        if(row_c.count(piece) > (self.board_size//2 + self.board_size%2)):
            return False

        col_c = self.board.get_col(col)
        col_c[row] = piece
        if not valid(col_c):
            return False

        if(col_c.count(piece) > (self.board_size//2 + self.board_size%2)):
            return False
        
        return True


class Board:
    """Representação interna de um tabuleiro de Takuzu."""

    def __init__(self, n, board):
        self.size = n
        self.board = board
    
    def __str__(self):
        board_str = ""
        for i in range(self.size):
            for j in range(self.size):
                board_str += str(self.get_number(i, j))
                if(j != self.size-1):
                    board_str += '\t'
            board_str += '\n'
            
        return board_str

    def get_size(self):
        return self.size

    def get_number(self, row: int, col: int) -> int:
        """Devolve o valor na respetiva posição do tabuleiro."""
        # TODO

        if(row > self.size-1 or row < 0 or col < 0 or col > self.size-1):
            raise ValueError("Board: given position does not exist in the current board.", row, " : ", col)

        return self.board[row][col]

    def check_value(self, row: int, col: int, value: int):
        """Checks if the given position's value is equal to the given value"""

        return self.get_number(row, col) == value

    def set_value(self, row: int, col: int, value: int):
        """Sets the value of a certain position in the board."""

        if self.check_value(row, col, value):
            return # dont know if we need this
        if(value not in (0, 1 , 2)):
            raise ValueError("Board: values must be 0, 1 or 2.")
        self.board[row][col] = value

        return self

    def adjacent_vertical_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente abaixo e acima,
        respectivamente."""
        # TODO

        if(row == 0):
            return (self.get_number(row + 1, col), None)

        if(row == self.size-1):
            return (None, self.get_number(row -1, col))

        return (self.get_number(row + 1, col), self.get_number(row - 1, col))

    def adjacent_horizontal_numbers(self, row: int, col: int):
        """Devolve os valores imediatamente à esquerda e à direita,
        respectivamente."""
        # TODO

        if(col == 0):
            return (None, self.get_number(row, col + 1))

        if(col == self.size-1):
            return (self.get_number(row, col - 1), None)

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
        # TODO (DONE?)
        
        from sys import stdin
        n = int(stdin.readline())
        board = list()
        for i in range(n):
            buffer = stdin.readline()
            row = [int(i) for i in buffer.split()]
            board.append(row)

        return Board(n, board)

    # TODO: outros metodos da classe

    def get_board(self):
        return self.board

    def get_row(self, row):
        return self.board[row][:]

    def get_col(self, col):
        copy = list()
        for i in range(self.size):
            copy.append(self.board[i][col])
        return copy

    def get_copy(self):
        copy = list()
        for row in self.board:
            copy.append(row[:])
        return copy

# check for number of equal consecutive values
def valid(row_or_column):
    n = 2
    c = 0
    for el in row_or_column:
        if(el == 2):
            c = 0
        elif(el == n):
            c += 1
        else:
            n = el
            c = 1
        if(c >= 3):
            return False
    return True

class Takuzu(Problem):

    def __init__(self, board: Board):
        """O construtor especifica o estado inicial."""
        # TODO
        Problem.__init__(self, TakuzuState(board))

    def actions(self, state: TakuzuState):
        """Retorna uma lista de ações que podem ser executadas a
        partir do estado passado como argumento."""
        # TODO

        board = state.get_board()
        actions = list()

        for i in range(state.board_size):
            for j in range(state.board_size):
                if(board[i][j] == 2):
                    if(state.valid_action(i, j, 0)):
                        actions.append((i, j, 0))
                    if(state.valid_action(i, j, 1)):
                        actions.append((i, j, 1))
                    return actions

        return actions

    def result(self, state: TakuzuState, action):
        """Retorna o estado resultante de executar a 'action' sobre
        'state' passado como argumento. A ação a executar deve ser uma
        das presentes na lista obtida pela execução de
        self.actions(state)."""
        # TODO

        board = Board(state.board_size, state.board.get_copy())
        new_state = TakuzuState(board.set_value(action[0], action[1], action[2]))

        return new_state

    def goal_test(self, state: TakuzuState):
        """Retorna True se e só se o estado passado como argumento é
        um estado objetivo. Deve verificar se todas as posições do tabuleiro
        estão preenchidas com uma sequência de números adjacentes."""
        # TODO

        board_l = state.get_board()

        board_t = [list(i) for i in zip(*board_l)]

        # check if all positions are filled
        for row in board_l:
            if row.count(2) != 0:
                return False

        for row in board_l:
            if not valid(row):
                return False

        for column in board_t:
            if not valid(column):
                return False

        # check if rows have the same number of 0s and 1s
        for row in board_l:
            if(state.board_size % 2 == 0):
                if(row.count(0) != row.count(1)):
                    return False
            else:
                if(abs(row.count(0) - row.count(1)) != 1): # QUESTION: can it be zero?
                    return False

        # check if columns have the same number of 0s and 1s
        for row in board_t:
            if(state.board_size % 2 == 0):
                if(row.count(0) != row.count(1)):
                    return False
            else:
                if(abs(row.count(0) - row.count(1)) != 1): # QUESTION: can it be zero?
                    return False

        # checking if all rows are different
        duplicate_rows = {tuple(x) for x in board_l if board_l.count(x) > 1}

        if(len(duplicate_rows) != 0):
            return False

        # checking if all columns are different
        duplicate_columns = {tuple(x) for x in board_t if board_t.count(x) > 1}
        
        if(len(duplicate_columns) != 0):
            return False

        return True

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

    
    # Ler tabuleiro do ficheiro 'i1.txt' (Figura 1):
    # $ python3 takuzu < i1.txt
    board = Board.parse_instance_from_stdin()
    problem = Takuzu(board)

    # search algorithm
    goal_node = depth_first_tree_search(problem)

    print(goal_node.state.board, sep="", end="")
