# Exercise 1 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement


class Animals():
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy
    def eat(self, food):
        self.energy = self.energy + (food * 10)
        # self.energy += food
        print(f'{self.name} has ate {food} blocks of food. His energy is now {self.energy}')
    def sleep(self, sleep):
        self.energy = self.energy + sleep
        print(f"{self.name} has slept for {sleep} minutes. His energy is now {self.energy}")
    def play(self, play):
        self.energy = self.energy - play
        print(f"{self.name} has played for a total of {play} minutes. His energy is now {self.energy}")
    
        
        
dog = Animal('Buddy', 10)
puppy = Animal('Lotus')
dog.play(5)  # -> "Buddy is playing for 5 minutes. His energy is now 5"
dog.sleep(10) # -> "Buddy is sleeping for 10 minutes. His energy is now 15"
puppy.play(30)
puppy.eat(2)
puppy.sleep(30)



# Exercise 2 - Turn the shopping cart program into an object-oriented program

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    
    
    def __init__(self, item, price):
        self.item = item
        self.price = price
        self.shopping_cart = []

    #Create a function for adding items, removing items, and showing the cart
    def add(self, food):
        food = input("What would you like to add to your cart today?")
        self.shopping_cart.append(food)
        print(f'{food.name.title()} has been added to your cart.')


    def remove(self, food):
        self.shopping_cart.remove(food)
        print(f'{food.name} has been removed from your cart.')

    def show(self):
        print(f'Your Shopping Cart: \n{self.shopping_cart}')


class dfood:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity



food1 = dfood("Apples", 8)
food2 = dfood("Oranges", 3)
food3 = dfood("Coconuts", 3)
food4 = dfood("Papaya", 4)

Cart.add(food1)
Cart.show()
Cart.add(food2)
Cart.add(food3)
Cart.add(food4)
Cart.show()
Cart.remove(food3)
Cart.show()