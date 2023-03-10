from board import *
from ship import *
from random import *
from dot import *
from myexceptions import *
from player import *


def greet():
    print('____________________')
    print('  Приветствуем вас  ')
    print('       в игре       ')
    print('    морской бой     ')
    print('____________________')
    print(' формат ввода: x  y ')
    print(' x - номер строки   ')
    print(' y - номер столбца  ')


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = False

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for le in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), le, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def print_boards(self):
        print('-' * 20)
        print('Доска пользователя:')
        print(self.us.board)
        print('-' * 20)
        print('Доска компьютера:')
        print(self.ai.board)
        print('-' * 20)

    def loop(self):
        num = 0
        while True:
            self.print_boards()
            if num % 2 == 0:
                print('Ходит пользователь!')
                repeat = self.us.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print('-' * 20)
                print('Пользователь выиграл!')
                break

            if self.us.board.defeat():
                self.print_boards()
                print('-' * 20)
                print('Компьютер выиграл!')
                break
            num += 1

    def start(self):
        greet()
        self.loop()


g = Game()
g.start()
