from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        if self.color == 'white':
            next_row = row + 1
            if self.is_position_on_board((next_row, col)):
                moves.append((next_row, col))
        elif self.color == 'black':
            next_row = row - 1
            if self.is_position_on_board((next_row, col)):
                moves.append((next_row, col))

        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny teoreticky možné tahy střelce (diagonální pohyb).
        """
        row, col = self.position
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)] 

        for dr, dc in directions:
            for i in range(1, 8): 
                new_row = row + dr * i
                new_col = col + dc * i
                move = (new_row, new_col)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny teoreticky možné tahy věže (horizontální a vertikální pohyb).
        """
        row, col = self.position
        moves = []
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dr, dc in directions:
            for i in range(1, 8):
                new_row = row + dr * i
                new_col = col + dc * i
                move = (new_row, new_col)
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny teoreticky možné tahy dámy (kombinace věže a střelce).
        """
        rook_moves = Rook(self.color, self.position).possible_moves()
        bishop_moves = Bishop(self.color, self.position).possible_moves()
        return rook_moves + bishop_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'



class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále (jedno pole ve všech směrech).
        """
        row, col = self.position
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                new_row = row + dr
                new_col = col + dc
                move = (new_row, new_col)

                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'




if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
