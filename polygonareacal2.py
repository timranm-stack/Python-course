from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        # Encapsulated attributes (conventionally "private")
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        if value <= 0:
            raise ValueError("Width must be positive.")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self) -> float:
        return self._width * self._height

    def __repr__(self):
        return f"Rectangle(width={self._width}, height={self._height})"


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    @property
    def side(self) -> float:
        return self._width

    @side.setter
    def side(self, value: float):
        if value <= 0:
            raise ValueError("Side must be positive.")
        self._width = value
        self._height = value

    def __repr__(self):
        return f"Square(side={self._width})"


class Circle(Shape):
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    def __repr__(self):
        return f"Circle(radius={self._radius})"


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self._base = base
        self._height = height

    @property
    def base(self) -> float:
        return self._base

    @base.setter
    def base(self, value: float):
        if value <= 0:
            raise ValueError("Base must be positive.")
        self._base = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    def area(self) -> float:
        return 0.5 * self._base * self._height

    def __repr__(self):
        return f"Triangle(base={self._base}, height={self._height})"


def main():
    shapes: list[Shape] = []

    while True:
        print("\nPolygon Area Calculator")
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Triangle")
        print("5. Show all shapes and areas")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            w = float(input("Width: "))
            h = float(input("Height: "))
            shapes.append(Rectangle(w, h))

        elif choice == "2":
            s = float(input("Side: "))
            shapes.append(Square(s))

        elif choice == "3":
            r = float(input("Radius: "))
            shapes.append(Circle(r))

        elif choice == "4":
            b = float(input("Base: "))
            h = float(input("Height: "))
            shapes.append(Triangle(b, h))

        elif choice == "5":
            if not shapes:
                print("No shapes created yet.")
            else:
                print("\nShapes and their areas (polymorphic call):")
                for i, shape in enumerate(shapes, start=1):
                    print(f"{i}. {shape} -> area = {shape.area():.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
