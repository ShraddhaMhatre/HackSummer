from game import Game

def main():
  while True:
    Game.print_menu()
    choice = int(input("\nYour choice: "))

    if choice == 1:
      pass
      # new game
      new_game = Game()
      new_game.game_loop()
    elif choice == 2:
      high_scores = Game.load_high_scores()
      Game.print_high_scores(high_scores)
    elif choice == 3:
      print("\nBye!")
      break
    else:
      print("\nNot a choice!\n")

main()
