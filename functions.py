import spooder

def constructProgress(word, guesses):
    out = ""
    for i in range(word.__len__()):

        ch = word[i]
        if ch == " ":
            out += "\n                 "
        else:
            if checkGuessesFor(ch, guesses):
                out += "  " + ch.upper()
            else:
                out += "  _"
    return out


def win(word, guesses):
    print("  YOUR PROGRESS:   " + constructProgress(word, guesses))
    print(spooder.spiders[11])
    print("You win! The word was " + word.upper() + ".")


def checkGuessesFor(x, guesses):
    for guess in guesses:
        if x == guess[0]:
            return True
    return False


def lose(word):
    print(spooder.spiders[10])
    print("The spider has discovered you and killed you 💀 \nThe word was " + word.upper() + ".")


def clear(guessesLeft):
    for i in range(100):
        print("\n")
    print(spooder.spiders[abs(guessesLeft - 10)])


def wrongAnswers(guesses):
    message = "You have already tried these incorrectly: "
    wrongdetected = False
    for guess in guesses:
        if guess[1] == 1:
            wrongdetected = True
            if guess[0] == guesses[guesses.__len__() - 1][0]:
                message += guess[0].upper() + "."
            else:
                message += guess[0].upper() + ", "
    if wrongdetected:
        print(message)