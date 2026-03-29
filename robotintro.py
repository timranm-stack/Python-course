class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, I am {self.name}!")

# Creating Harsh's robots
tom = Robot("Tom")
jerry = Robot("Jerry")

# Robots introducing themselves
tom.introduce()
jerry.introduce()
