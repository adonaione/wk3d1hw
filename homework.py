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
    def add(self, item):
        #add item to list
        lst = self.shopping_list.append(item)
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
        

class food:
    def __init__(self, item, quantity):
        self.item = item 
        self.quantity = quantity    



food1 = food("Apples", 8)
food2 = food("Oranges", 3)
food3 = food("Coconuts", 3)
food4 = food("Papaya", 4)


Cart.add(food1)
Cart.show()
Cart.add(food2)
Cart.add(food3)
Cart.add(food4)
Cart.show()
Cart.remove(food3)
Cart.show()