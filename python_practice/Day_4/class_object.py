class Monster:

    def __init__(self,color,legs): # constructor / python magic mathod
        self.color = color
        self.legs = legs

    def eats(self): # method, not function
            print("I eats deer. {}".format(self.color))

tiger = Monster('Yellow', 4)


print("I am tiger. My Color is {}.I have {} heads.".format(tiger.color,tiger.legs))
tiger.eats()

class Animal(Monster): # inheritence
    def attack(self):
        print("Huhu hu hu")
tiger = Monster('Yellow', 4)


print("I am tiger. My Color is {}.I have {} heads.".format(tiger.color,tiger.legs))
tiger.eats()
tiger.attack()


# inheritance , multi level , multiple inheritance