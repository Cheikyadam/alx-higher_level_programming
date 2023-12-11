"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """ Class rectangle

    Attributes:
        x (int)
        y (int)
        width (int)
        height (int)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor with all attributes"""
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    @property
    def x(self):
        """to retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """to update x value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """To retrieve y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """Updating y with value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """To retrieve width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Update witdh value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("witdh must be > 0")
        self.__width = value

    @property
    def height(self):
        """To retrieve height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """"Update height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """To calculate area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """To display rectangle"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for t in range(self.__x):
                    print(' ', end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Printing rectangle infos"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args):
        """To update rectangle value"""
        nb = len(args)
        if nb != 0:
            if nb >= 1:
                self.id = args[0]
            if nb >= 2:
                self.width = args[1]
            if nb >= 3:
                self.height = args[2]
            if nb >= 4:
                self.x = args[3]
            if nb >= 5:
                self.y = args[4]
