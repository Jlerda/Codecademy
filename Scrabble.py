letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points={key:value for key, value in zip(letters, points)}

letter_to_points[" "]=0

def score_word(word):
  point_total=0
  for letter in word:
    letter_checked=letter.upper()
    if letter_checked not in letter_to_points:
      point_total+=0
    else:
      point_total+=letter_to_points[letter_checked]
    
  return point_total

#brownie_points=score_word("Brownie")
#print(brownie_points)

player_to_words={"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    print(player + " is not an actual player.")

def update_point_totals(): 
  player_to_points={}
  for player in player_to_words:
    player_points=0
    for word in player_to_words[player]:
      player_points+=score_word(word)
    player_to_points[player]=player_points
  
  return player_to_points

def the_winner_is(player_to_points):
  winner=""
  winner_points=0
  for player in player_to_points:
    if int(player_to_points[player])>winner_points:
      winner_points=player_to_points[player]
      winner=player
  
  return winner + " win the game with a score of "+str(winner_points)+"!"

#play_word("player2", "ABCD")
#play_word("player1", "ABCD")
#print(update_point_totals())
#print(the_winner_is(update_point_totals()))
