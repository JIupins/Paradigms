class Coffee:
    def cost(self):
        return 10


class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        pass


class Sugar(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 2


class Milk(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 5


coffee = Coffee()
coffee_with_sugar = Sugar(coffee)
coffee_with_milk = Milk(coffee_with_sugar)

print(coffee_with_milk.cost())