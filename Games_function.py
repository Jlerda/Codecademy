import random

money = 100

def flipping_coin(money_bet, call):
  callvalor=0
  if call=="Heads":
    callvalor=1
  else:
    callvalor=2
  flipcoin=random.randint(1,2)
  if flipcoin==1:
    print("It's heads!")
  else:
    print("It's tails!")

  if flipcoin==callvalor:
    print("You have won {amount}".format(amount=money_bet))
    return money_bet
  else:
    print("Yuo have lost {amount}".format(amount=-(money_bet)))
    return -money_bet

# flipping_coin(30, "Heads")

def Cho_Han(money_bet, call):
  dice1=random.randint(1,6)
  print("The first dice is {valor}!".format(valor=dice1))
  dice2=random.randint(1,6)
  print("The second dice is {valor}!".format(valor=dice2))
  if (dice1+dice2)%2==0 and call=="Even":
    print("You have won {amount}".format(amount=money_bet))
    return money_bet
  
  elif (dice1+dice2)%2!=0 and call=="Odd":
    print("You have won {amount}".format(amount=money_bet))
    return money_bet
  
  else:
    print("You have lost {amount}".format(amount=-money_bet))
    return -money_bet

# Cho_Han(40, "Odd")

def Higher_card(money_bet): #The player of the previous games is player1 in this game
  deck=[]
  for i in range(4):
    for j in range(1, 14):
      deck.append(int(j))    
  player1=random.randint(1,13)
  print("The first player has valor {}".format(player1))
  deck.remove(player1)
  player2=int(random.sample(deck, 1)[0])
  print("The second player has valor {}".format(player2))
  if player1>player2:
    print("The first player win {}!".format(money_bet))
    return money_bet
  elif player2>player1:
    print("The second player win {}!".format(money_bet))
    return -money_bet
  else:
    print("It's a tie!")
    return 0

# Higher_card(50)

def Roulette(money_bet, call):
  roulette_chances=[i for i in range(37)]+["00"]
  roulette_valor=int(random.sample(roulette_chances, 1)[0])
  print("It's a {}!".format(roulette_valor))
  if call=="Odd" and roulette_valor%2!=0 and roulette_valor!=0:
    print("You win {} dollars!".format(money_bet))
    return money_bet
  elif call=="Even" and roulette_valor%2==0 and roulette_valor!=0:
    print("You win {} dollars!".format(money_bet))
    return money_bet
  elif call==roulette_valor:
    print("You win a lot! {} dollars!!".format(money_bet*35))
    return money_bet*35
  else:
    print("I'm sorry you lose {} dollars!!".format(money_bet))
    return -money_bet


# Roulette(3,"Odd")

money += flipping_coin(20, "Heads")
money += Cho_Han(30, "Odd")
money += Higher_card(40)
money += Roulette(60, "Even")

print(money)





  

