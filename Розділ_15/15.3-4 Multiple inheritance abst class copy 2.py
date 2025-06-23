class Figure:
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__length = length
        self.__width = width

    def move(self, new_x: int, new_y: int) -> None:
        self.__pos_x = new_x
        self.__pos_y = new_y

    def resize(self, new_length: int, new_width: int) -> None:
        self.__length = new_length
        self.__width = new_width

class Rectangle(Figure):
    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        super().__init__(pos_x, pos_y, length, width)

class Square(Figure):
    def __init__(self, pos_x: int, pos_y: int, length: int) -> None:
        super().__init__(pos_x, pos_y, length, length)

# Використання
rect_1 = Rectangle(0, 0, 10, 5)
rect_1.move(5, 5)

square_1 = Square(0, 0, 10)
square_1.resize(20, 20)

print(f"Rectangle position: ({rect_1._Figure__pos_x}, {rect_1._Figure__pos_y}), "
      f"size: ({rect_1._Figure__length}, {rect_1._Figure__width})")

print(f"Square position: ({square_1._Figure__pos_x}, {square_1._Figure__pos_y}), "
      f"size: ({square_1._Figure__length}, {square_1._Figure__width})")
