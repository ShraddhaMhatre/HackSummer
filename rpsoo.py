import random
import pickle

class Game:
  MENU_OPTIONS = {
    1: "New Game",
    2: "High Scores",
    3: "Quit"
  }

  INIT_SCORE = {
    "wins": 0,
    "losses": 0,
    "ties": 0
  }

  BEATS = {
  "rock": "scissors",
  "paper": "rock",
  "scissors": "paper"
}

  HIGH_SCORES_FILE = "highscores.pickle"


  @classmethod
  def update_high_scores(cls, high_scores):
      with open(cls.HIGH_SCORES_FILE,"wb") as f:
        pickle.dump(high_scores,f)

  @classmethod
  def load_high_scores(cls):
    try:
      with open(cls.HIGH_SCORES_FILE,"rb") as f:
        high_scores = pickle.load(f)
    except:
      high_scores = {}
    finally:
      return high_scores

  @classmethod
  def compare(cls, player_choice, computer_choice):
    if Game.BEATS[player_choice] == computer_choice:
      return "WIN"
    elif Game.BEATS[computer_choice] == player_choice:
      return "LOSS"
    else:
      return "TIE"

  @classmethod
  def print_menu(cls):
    print("\nChoose one: ")
    for m in cls.MENU_OPTIONS:
      print("{}: {}".format(m,cls.MENU_OPTIONS[m]))
  
  @classmethod
  def print_choices(cls):
    print("\nChoose one: ")
    for b in cls.BEATS:
      print(b)
    print("\nPress q to quit\n")

  @classmethod
  def print_score(cls,score):
    for k in score:
      print("{}:{}".format(k, score[k]))

  @classmethod
  def print_high_scores(cls,high_scores):
    print("\n===HIGH SCORES===\n")
    for p in high_scores:
      print("{}\n\n".format(p))
      cls.print_score(high_scores[p])

  @classmethod
  def get_player_name(cls):
    return input("\nEnter player name: ")

  def __init__(self):
    self.player = Game.get_player_name()
    self.score = Game.INIT_SCORE
    self.high_scores = Game.load_high_scores()
  
  @classmethod
  def get_player_choice(cls):
    return input("\nYour choice: ")

  @classmethod
  def get_computer_choice(cls):
    choices = list(cls.BEATS.keys())
    return random.choice(choices)

  def check_high_score(self):
    try:
      high_score = self.high_scores[self.player]
    except KeyError:
      return True
    try:
      weighted_high = high_score["wins"] - high_score["losses"]
      weighted_current = self.score["wins"] - self.score["losses"]
      return weighted_current > weighted_high
    except KeyError:
      return True

  def handle_result(self,result):
    if result == "WIN":
      self.score["wins"] += 1
      print("\nYou Won!\n")
    elif result == "LOSS":
      self.score["losses"] += 1
      print("\nYou have lost it!\n")
    else:
     self.score["ties"] += 1
     print("\nIt's a Tie!\n")

  def game_loop(self):
    while True:
      Game.print_choices()
      player_choice = Game.get_player_choice()
      if player_choice == "q":
        print("\nGood game, {}".format(self.player))
        print("\nFinal Score:\n")
        Game.print_score(self.score)

        if self.check_high_score():
          print("\nNew High Score:\n")
          self.high_scores[self.player] = self.score
          Game.update_high_scores(self.high_scores)
        break

      elif player_choice in Game.BEATS:
        computer_choice = Game.get_computer_choice()
        print("\nComputer choice: {}\n".format(computer_choice))
        result = Game.compare(player_choice, computer_choice)
        #Handle result
        self.handle_result(result)
        Game.print_score(self.score)
      else:
        print("\nIncorrect choice")