import random
import pickle #to save high score
#.Pickle file is not human-readable and it is still not secure as you can update the file

HIGH_SCORES_FILE = "highscores.pickle"

#BEATS
BEATS = {
  "rock": "scissors",
  "paper": "rock",
  "scissors": "paper"
}

"""
HIGH SCORES
Load high SCORES
Check if score is new high score
Update high score
"""

#Load high scores
def load_high_scores():
  try:
    with open(HIGH_SCORES_FILE,"rb") as f:
      high_scores = pickle.load(f)
  except:
    high_scores = {}
  finally:
    return high_scores

#Check high scores
def check_high_score(high_scores, score):
  try:
    weighted_high = high_scores["wins"] - high_scores["losses"]
    weighted_current = score["wins"] - score["losses"]
    return weighted_current > weighted_high
  except KeyError:
    return True

#Update high scores
def update_high_scores(score):
  with open(HIGH_SCORES_FILE,"wb") as f:
    pickle.dump(score,f)

#Print choices
def print_choices():
  print("\nChoose one: ")
  for b in BEATS:
    print(b)
  print("\nPress q to quit\n")

#Get player's choice
def get_player_choice():
  return input("\nYour choice: ")

#Get computer's choice
def get_computer_choice():
  choices = list(BEATS.keys())
  return random.choice(choices)

#Compare choices
def compare(player_choice, computer_choice):
  if BEATS[player_choice] == computer_choice:
    return "WIN"
  elif BEATS[computer_choice] == player_choice:
    return "LOSS"
  else:
    return "TIE"

def handle_result(result, score):
  if result == "WIN":
    score["wins"] += 1
    print("\nYou Won!\n")
  elif result == "LOSS":
    score["losses"] += 1
    print("\nYou have lost it!\n")
  else:
    score["ties"] += 1
    print("\nIt's a Tie!\n")

def print_score(score):
  for k in score:
    print("{}:{}".format(k, score[k]))
    
def game_loop():
  score = {
    "wins":0,
    "losses":0,
    "ties":0
  }
  """
  Order of play:

  Player chose R, P, S
  Computer chooses R, P, S
  Compare choices:
  R > S
  P > R
  S > P
  Win, Loss, Tie
  Keep Score
  """
  while True:
    high_score = load_high_scores()
    print_choices()
    player_choice = get_player_choice()
    if player_choice == "q":
      print("\nThanks for playing!\n")
      print("\nFinal Score: \n")
      print_score(score)
      if check_high_score(high_score,score):
        print("\nNew High Score!\n")
        update_high_scores(score)
      break
    if player_choice in BEATS:
      computer_choice = get_computer_choice()
      print("\nComputer choice: {}\n".format(computer_choice))
      result = compare(player_choice, computer_choice)
      #Handle result
      handle_result(result, score)
      print_score(score)
    else:
      print("\nIncorrect choice")

game_loop()