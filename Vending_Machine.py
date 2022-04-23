'''Coffe Vending Machine'''





from ast import While
from re import I


class Menu: # show all menu in the screen
  def Three_choice(self):
    file = int(input("1.Coffee 2.Beverage 3.Bread: "))
    return file
      
  def Coffee(self):

      coffee ={1:'Hot Coffee', 2:
      'Iced Coffee', 3:'Latte', 4:'Iced Latte'}
      i = 1
      while i<5:
        print("{0}.{1}".format(i,coffee.get(i)))
        i+=1
      a = int(input("Choose: "))

      return coffee.get(a)

  def Beverage(self):
      beverage = {1:'Apple Juice', 2:'PineApple Juice', 3:'Watermelon Juice', 4:'Orage Juice'}
      i = 1
      while i<5:
        print("{0}.{1}".format(i,beverage.get(i)))
        i+=1
      a = int(input("Choose: "))

      return beverage.get(a)
      
  def Bread(self):
    bread = {1:'Bagel', 2:'Croissant', 3:'Scone', 4:'Dougnut'}
    i = 1
    while i<5:
        print("{0}.{1}".format(i,bread.get(i)))
        i+=1
    a = int(input("Choose: "))

    return bread.get(a)

  def Drink(self, a):

    
    if a == 1:
      return self.Coffee()
     
    elif a == 2:
     return self.Beverage()

    else:
     return self.Bread()
    
  
     
    


class Buyer(Menu):

  def __init__(self,first,second):
    self.first  = first
    self.second = second
    


  def Price(self):
    coffee_price = {'Hot Coffee':2.25, 'Iced Coffee':2.75, 'Latte':3.5, 'Iced Latte':4}

    beverage_price = {'Apple Juice':3, 'PineApple Juice':3, 'Watermelon Juice':3.5, 'Orage Juice':3.5}

    bread_price = {'Bagel':4.5, 'Croissant':5, 'Scone':3.5, 'Dougnut':2}

    
    if self.first == 1:
      
      return coffee_price.get(self.second)
    elif self.first == 2:
      return beverage_price.get(self.second)
    else:
      return bread_price.get(self.second)
  
      
ini_value = Menu()
cate=  ini_value.Three_choice()
print(cate)
food = ini_value.Drink(cate)

Jaesung = Buyer(cate, food)
print('{0}: ${1}'.format(food,Jaesung.Price()))







 
        
      

