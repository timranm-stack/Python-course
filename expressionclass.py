class Expression:
    def __init__(self, num1, num2, num3):
        # instance attributes
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_numbers(self):
        result = self.num1 + self.num2 + self.num3
        print(f"The sum of {self.num1}, {self.num2}, and {self.num3} is: {result}")
        return result


# creating objects and using the method
expr1 = Expression(1, 2, 3)
expr1.add_numbers()

expr2 = Expression(10, 20, 30)
expr2.add_numbers()
