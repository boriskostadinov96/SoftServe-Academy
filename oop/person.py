class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food):
        if food in self.likes:
            return f"{self.name} eats the {food} and loves it!"

        elif food in self.hates:
            return f"{self.name} eats the {food} and hates it!"

        else:
            return f"{self.name} eats the {food}!"


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))