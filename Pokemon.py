class Pokemon:
  def __init__(self, name, level, element, maximum_health, ko=False):
    self.name = name
    self.level = level
    self.element = element
    self.maximum_health = maximum_health * level
    self.current_health = self.maximum_health
    self.ko = ko
  
  def __repr__(self):
    return str(self.name)

  def lose_health(self, health_loss):
    self.current_health -= health_loss
    if self.current_health <= 0:
      self.current_health = 0
    print (self.name +" has lost "+str(health_loss)+" now his health is "+ str(self.current_health) + "\n")
    if self.current_health ==0:
      Pokemon.knock_out(self)
  
  def regain_health(self, health_gain):
    self.current_health += health_gain
    if self.current_health > self.maximum_health:
      self.current_health = self.maximum_health
    print(self.name +" has gain "+str(health_gain)+" now his health is "+ str(self.current_health) + "\n")

  def knock_out(self):
    if self.current_health <= 0:
      self.current_health = 0
      self.ko = True
      print(self.name +" is knocked out!\n")
    else:
      print(self.name +" is not knocked out! His health is "+str(self.current_health)+"\n")
    
  def revive(self):
    if self.ko == True:
      self.current_health = self.maximum_health//2
      self.ko = False
      print(self.name +" had been revived! Now his health is "+ str(self.current_health)+"\n")
    else:
      print(self.name +" is alive yet!\n")
    
  def attack(self, Pokemon):
    if self.ko == False:
      if self.element == "Fire" and Pokemon.element == "Grass":
        print(self.name + " is attacking " + Pokemon.name + "!\n")
        print(self.name + " deals " + str(self.level*2)+ " damage!\n")
        Pokemon.lose_health(self.level*2)
      elif self.element == "Water" and Pokemon.element == "Fire":
        print(self.name + " is attacking " + Pokemon.name + "!\n")
        print(self.name + " deals " + str(self.level*2)+ " damage!\n")
        Pokemon.lose_health(self.level*2)
      elif self.element == "Grass" and Pokemon.element == "Water":
        print(self.name + " is attacking " + Pokemon.name + "!\n")
        print(self.name + " deals " + str(self.level*2)+ " damage!\n")
        Pokemon.lose_health(self.level*2)
      else:
        print(self.name + " is attacking " + Pokemon.name + "!\n")
        print(self.name + " deals " + str(self.level/2)+ " damage!\n")
        Pokemon.lose_health(self.level/2)
    else:
      print(self.name + " cannot attack!\nHe is knocked out!\n")

charmander=Pokemon("Charmander", 13, "Fire", 20)
bulbasaur=Pokemon("Bulbasaur", 10, "Grass", 20)
scyther=Pokemon("Scyther", 20, "Grass", 20)
charizard=Pokemon("Charizard", 50, "Fire", 20)
wartortle=Pokemon("Wartortle", 24, "Water", 20)
suicune=Pokemon("Suicune", 65, "Water", 20)


class Trainer:
  def __init__(self, name, potions, roster, active=0):
    self.name = name
    self.potions = potions
    self.roster = roster
    self.active = active

  def use_potions(self):
    if self.potions>0:
      print(self.name + " use a healing potion!\n")
      self.roster[self.active].regain_health(80)
    else:
      print("You don't have any potions left.\n")
  
  def trainer_attack(self, Trainer):
    print(self.name + " is attacking " + Trainer.name + "!\n")
    self.roster[self.active].attack(Trainer.roster[Trainer.active])

  def switch(self, int):
    if self.roster[int]!= "" and (self.roster[int]).ko==False: 
      self.active = int
      print(self.name + " switch to " + str(self.roster[self.active]) + "!\n")
    elif self.roster[int]=="":
      print("You don't have any pokemon in this slot.\n")
    else:
      print(str((self.roster[int]))+ " is knocked out!\nYou cannot switch to him!\n")
    
ash=Trainer("Ash", 3, [charizard, wartortle, charmander, scyther, suicune, bulbasaur])
brock=Trainer("Brock", 4, [suicune, charmander, wartortle, bulbasaur, charizard, scyther])

# brock.switch(3)
# ash.trainer_attack(brock)
# ash.trainer_attack(brock)
# brock.switch(0)
# brock.switch(3)



# charizard.attack(bulbasaur)
# charizard.attack(bulbasaur)
# charizard.attack(bulbasaur)
# bulbasaur.attack(charizard)
# ash.trainer_attack(brock)
# brock.switch(2)
# brock.trainer_attack(ash)
# brock.use_potions()

# bulbasaur.attack(charmander)
# charmander.lose_health(50)
# charmander.regain_health(30)
# charmander.revive()
# charmander.lose_health(240)
# charmander.revive()
'''Add more functionality that we haven’t implemented yet. Here is a list of ideas that you might want to try:
Give Pokémon experience for battling other Pokémon. A Pokémon’s level should increase once it gets enough experience points.
Create specific Classes that inherit from the general Pokémon class. For example, could you create a Charmander class that has all of the functionality of a Pokémon plus some extra features?
Let your Pokémon evolve once they hit a certain level.
Have more stats associated with a Pokémon. In the real game, every Pokémon has stats like Speed, Attack, Defense. All of those stats effect the way Pokemon battle with each other. For example, the Pokémon with the larger Speed stat will go first in the battle.'''
