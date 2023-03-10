# -*- coding: utf-8 -*-
"""Assignment_6_JSON and OOP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JxaAcahXaPvEEBs2qAsgkJLD1iBJ4YtU
"""

########### OOPS ############

class Dog:
  def __init__(self, name, age, coat_color):
    self.name = name
    self.age = age
    self.coat_color = coat_color

  def description(self):
    print("Name:", self.name)
    print("Age:", self.age)

  def get_info(self):
    print("Coat color:", self.coat_color)
class JackRussellTerrier(Dog):
  def __init__(self, name, age, coat_color, breed, energy_level):
    super().__init__(name, age, coat_color)
    self.breed = breed
    self.energy_level = energy_level

  def get_breed(self):
    print("Breed:", self.breed)

  def get_energy_level(self):
    print("Energy level:", self.energy_level)
class Bulldog(Dog):
  def __init__(self, name, age, coat_color, breed, loyalty):
    super().__init__(name, age, coat_color)
    self.breed = breed
    self.loyalty = loyalty

  def get_breed(self):
    print("Breed:", self.breed)

  def get_loyalty(self):
    print("Loyalty:", self.loyalty)
dog1 =Dog("Charlie", 5, "Brown")
dog1.description()
dog1.get_info()

dog2 = JackRussellTerrier("Max", 3, "White", "Jack Russell Terrier", "High")
dog2.description()
dog2.get_info()
dog2.get_breed()
dog2.get_energy_level()

dog3 = Bulldog("Buddy", 7, "Black", "Bulldog", "Very high")
dog3.description()
dog3.get_info()
dog3.get_breed()
dog3.get_loyalty()









