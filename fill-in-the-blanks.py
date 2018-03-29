data = {
    "easy": {
    "phrase": "A ___1___ definition is an executable statement. Its "
    "execution binds the ___1___ name in the current local "
    "namespace to a ___1___ ___2___ (a ___3___ around the "
    "executable code for the ___1___). This ___1___ ___2___ "
    "contains a reference to the current ___4___ namespace as the "
    "___4___ namespace to be used when the ___1___ is called.",
    "answers": ["function", "object", "wrapper", "global"],
    "failures": 5
    },
    "medium": {
    "phrase": "The ___1___ statement is used for repeated "
    "execution as long as an expression is ___2___. This "
    "repeatedly tests the expression and, if it is ___2___, "
    "executes the first suite; if the expression is ___3___ "
    "(which may be the first time it is tested) the suite of "
    "the ___4___ clause, if present, is executed and the loop "
    "terminates.",
    "answers": ["while", "true", "false", "else"],
    "failures": 3
    },
    "hard": {
    "phrase": "Python knows a number of ___1___ data types, "
    "used to group together other values. The most versatile is "
    "the ___2___, which can be written as a ___3___ of "
    "comma-separated values (items) between ___3___ brackets. "
    "___2___s might contain items of different types, but usually "
    "the items all have the ___4___ type.",
    "answers": ["compound", "list", "square", "same"],
    "failures": 1
    }
}


def select_level():
    """Ask user to choose difficulty level.

    Set up while loop, use raw_input to ask user enter level
    if user's input valid, return the input, else keep running
    the loop.

    Args: 
        none

    Return: 
        levels: choosen by user
        output2-4: elements from data dictionary
        
    """
    while True:
        levels = raw_input("Please choose difficulty level by "
        "typing it in: easy, medium, or hard.").lower() 
        if levels in data:
            return (levels,
                    data[levels]["phrase"],
                    data[levels]["answers"],
                    data[levels]["failures"])
        else:
            print "Sorry, your input is not valid! Try again!"


def prompt(selected_level, selected_phrase, chance):
    """Send prompt message at the beginning of the game.

    Args:
        arg1 (str): level chosen by player
        arg2 (str): phrase from list - data
        arg3 (number): the failures from list - data

    Return:
        None (only print promt message)
    """
    print "You selected "+selected_level+"."
    print "You will get "+str(chance)+" chance(s)"
    print "The current paragraph reads as such:"
    print selected_phrase
    

def print_message(current_phrase):
    """function takes phrase as argument, and print it out"""
    print "\nCorrect!!"
    print "\nThe current paragraph reads as such:"
    print current_phrase


def game_over():
    """this function only print out Game Over!"""
    print "\nGame Over!"


def play_game():
    """This function is the main engine. All logic of the game is
    process by this function. This function defines 4 variables, 
    and manipulates phrase and chance until the blanks are filled or 
    player fails in their attempts.

    Args:
        None

    Return: 
        none (only print out some message)

    """
    level,phrase,answers,chance=select_level()
    hits=0 # record how many blanks space
    prompt(level, phrase, chance) # print prompt messages

    while hits<len(answers) and chance>0: 
        attempt=raw_input("\nFill in the ___"+str(hits+1)+"___").lower()
        if attempt in answers: 
        # if player's answer correct, goes here
            phrase=phrase.replace("___"+str(hits+1)+"___", attempt)
            hits += 1 # player hit the right answer, blank space number increment by 1
            print_message(phrase) # use helper function to print message
        else:
        # if player's answer incorrect, goes here, if is the last chance, game over
            if chance>1: 
                chance -= 1
                print "\nIncorrect! "+str(chance)+" chance(s) left."
            else:
                return game_over()

    print "\nYou Win!"


play_game()