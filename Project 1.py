
import random

number_str = input('Enter the number of beans: ')
number_int = int(number_str)
 #Setting the initial count of beans as input
    
class Thebeangame:

   def __init__(self):
           
       self.beansCount= number_int
      
   def is_over(self):
  
      
       if self.beansCount==0:
           return True
       else:
           return False
           
   def player_1_turn(self) :
  
       beansRemove=random.randint(1, 3)
      
       self.beansCount=self.beansCount-beansRemove
      
       if self.beansCount<0:
           self.beansCount=0
          
       print('player 1 removed {0} beans, {1} remaining'.format(beansRemove, self.beansCount))
      
       if self.beansCount==0:
           print('player 1 lost')
  
    
   def player_2_turn(self) :
  
       beansRemove=random.randint(1, 3)
          
       self.beansCount=self.beansCount-beansRemove
          
       if self.beansCount<0:
           self.beansCount=0
          
       print('player 2 removed {0} beans, {1} remaining'.format(beansRemove, self.beansCount))
      
       if self.beansCount==0:
           print('player 2 lost')


if __name__=='__main__':
  
   beans=Thebeangame()
  
   while not beans.is_over():
  
       beans.player_1_turn()
      
       if not beans.is_over():
           beans.player_2_turn() 
