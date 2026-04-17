class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def info(self):
            print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
            print("Bark")


class Lion:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def info(self):
          print(f"I am a lion. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
          print("Rroar")

cat1 = Cat("Lucky", 5)
dog1 = Dog("Root", 10)
lion1 = Lion("King", 13)

for animal in (cat1, dog1, lion1):
      animal.info()
      animal.make_sound()
