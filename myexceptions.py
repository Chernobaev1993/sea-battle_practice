# Общий класс, от которого будут наследоваться остальные исключения
class BoardException(Exception):
    ...


class BoardOutException(BoardException):
    def __str__(self):
        return 'Вы пытаетесь выстрелить за доску!'


class BoardUsedException(BoardException):
    def __str__(self):
        return 'Вы уже стреляли в эту клетку'


# Исключение чтобы правильно размещать корабли
class BoardWrongShipException(BoardException):
    ...
