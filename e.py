class Merchant:
    def __init__(self, name, products):  #Python uses __init__ to initialize class attributes.
        self.name = name
        self.products = products
    def sell(self, item):
        if item in self.products:
            self.products.remove(item)
            print(self.products)
        else:
            print(f"{item} is not available in the inventory.")
Nelson = Merchant("Nelson", ["Human", "poopy"])
Denis = Merchant("Denis", ["Zombie", "poop"])
Denis.sell("poop")