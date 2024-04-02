# Exercise 1 - Write a Python class for an Animal that has a name and energy attributes. The animal class should also have methods for eat, sleep, and play that will take in an integer and increase/decrease the energy of the animal with a formatted print statement

# Example 1
#create animal class
class Animal():
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy
    def eat(self, food):
        self.energy = self.energy + (food * 10)
        print(f'{self.name} has ate {food} cans of food. His energy is now {self.energy}')
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
puppy.play(60)
puppy.eat(2)
puppy.sleep(30)



# Exercise 2 - Turn the shopping cart program into an object-oriented program

# Create a class called cart that retains items and has methods to add, remove, and show
#create class for cart
class Cart:
    #def initalize cart with list to retain items 
    def __init__(self):
        # create empty list
        self.shopping_list = []
    
    #create method for adding
    def add(self, food):
        #add item to list
        lst = self.shopping_list.append(food)
        return lst
    
    # create method for removing
    def remove(self, item):
        # remove item from list
        lst = self.shopping_list.remove(item)
        return lst
    
    #create method for showing items in cart
    def show(self):
        # print list
        print(self.shopping_list)
        




cart = Cart()
food1 = "Apples"
cart.add(food1)

food2 = "Oranges"
food3 = "Coconuts"
food4 = "Papaya"
cart.show()
cart.add(food2)
cart.add(food3)
cart.add(food4)
cart.show()
cart.remove(food3)
cart.show()