import GenerateNumbers
import ScoreBoard

# setup
name = input('What is your name?\n')
sb = ScoreBoard.ScoreBoard(name, 3)


# game loop
def game_loop():
    done = False
    while done is False:
        print("Scores:")
        print(name + ": " + str(sb.getScorePlayer()))
        print("AI: " + str(sb.getScoreAi()))

        print("Time to roll!")
        gn = GenerateNumbers.GenerateNumbers(1, 20)
        pn = gn.getPlayerNumber()
        an = gn.getAiNumber()
        print("You roll: " + str(pn))
        print("AI rolls: " + str(an))
        if pn > an:
            print("You win the round!\n")
            sb.addScorePlayer(1)
        elif an > pn:
            print("AI wins the round!\n")
            sb.addScoreAi(1)
        else:
            print("Tied round!\n")

        # Check for winner
        if sb.getScorePlayer() >= sb.winningGoal:
            done = True
            print("You win the game!")
        if sb.getScoreAi() >= sb.winningGoal:
            done = True
            print("AI wins the game!")

game_loop()