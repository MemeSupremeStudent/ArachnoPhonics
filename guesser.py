import random
import Alphabet
import functions as work
import dictionary

#ask the user for input
#if input is in the word and is not yet in correct guesses, add it to correct guesses
#if correct guesses contain all letters of the random word, end the loop






def run():
    words = dictionary.word_list
    guesses = []
    word = random.choice(words)
    print("Welcome to ArachnoPhonics! \nHere are the rules:\n  *You must guess the entire word before the spiders see you!\n  *You cant guess the same thing multiple times\n  *You can only guess one LETTER at a time\n\n   Have fun!")
    guessesLeft = 10

    while True:

        work.wrongAnswers(guesses)
        print("\n  YOUR PROGRESS: " + work.constructProgress(word, guesses) + "\n")
        guess = input("Guess a letter: ").lower()
        if guess in Alphabet.list:
            if not work.checkGuessesFor(guess, guesses):
                if guess in word:
                    guesses.append([guess, 0])
                    print("\n    Correct!\n")
                    if "_" not in work.constructProgress(word, guesses):
                        work.win(word, guesses)
                        break
                    else:
                        work.clear(guessesLeft)
                else:
                    guessesLeft -= 1
                    if guessesLeft == 0:
                        work.lose(word)
                        break
                    else:
                        work.clear(guessesLeft)
                        print("Incorrect! " + str(guessesLeft) + " guesses left...")
                        guesses.append([guess, 1])

            else:
                work.clear(guessesLeft)
                print("You already guessed that!")
                pass
        else:
            work.clear(guessesLeft)
            print("Please enter one letter only!")
            pass




Running = True
while Running:
    run()
    userinput = ""
    while True:
        userinput = input("Would you like to play again? (y/n)").lower()
        if userinput == "n":
            Running = False
            break
        elif userinput == "y":
            for i in range(100):
                print("\n")
            break
        else:
            print("Please enter y or n")
