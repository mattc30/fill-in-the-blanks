data = {
    "easy": {
    "phrase": "A ___1___ definition is an executable statement. Its"
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


def select_level ():
    """Ask user to choose difficulty level.

    Set up while loop, use raw_input to ask user enter level
    if user's input valid, return the input, else keep running
    the loop.

    Args: 
        none

    Return: 
        easy, medium, or hard in string

    """
    while True:
        level = raw_input("Please choose difficulty level by "
        "typing it in: easy, medium, or hard.").lower() 
        if level in data:
            return level
        else:
            print "Sorry, your input is not valid! Try again!"


def prompt (level, selected_phrase, chance):
    """Send prompt message at the beginning of the game.

    Args:
        arg1 (str): level chosen by player
        arg2 (str): phrase from list - data
        arg3 (number): the failures from list - data

    Return:
        None (only print promt message)
    """
    print "You selected " + level + "." + \
    "\nYou will get " + str(chance) + " guess(es) per blank" + \
    "\nThe current paragraph reads as such:" + \
    "\n" + selected_phrase


def play_game(level):
    """This function is the main engine. All logic of the game is
    process by this function. This function defines three variables, 
    and manipulates phrase and chance until the blanks are filled or 
    player fails in their attempts.

    Args: the level choosen by player

    Return: none (only print out some message)

    """
    answers = data[level]["answers"] # from data dictionary
    phrase = data[level]["phrase"] # from data dictionary
    chance = data[level]["failures"] # from data dictionary
    hits = 0 # this is the index of answers
    prompt(level, phrase, chance) # print prompt messages
    while hits < len(answers) and chance > 0: 
        attempt_answer = raw_input('\nFill in the __' + \
        str(hits + 1) + '__\n').lower() # ask player enter answer
        if attempt_answer == answers[hits]: # if user's answer is right goes to here
            if hits != (len(answers)-1): # if is not the last answer, print message
                phrase = phrase.replace("___"+str(hits+1)+"___", \
                answers[hits]) # replace element for print out later
                print "\nCorrect!" + \
                "\nThe current paragraph reads as such:" + \
                "\n" + phrase
                chance = data[level]["failures"] # chance has to be reseted when testing a new element
                hits += 1
            else: # if is last answer, return winning message and break the loop
                print "\nYou Win!!"
                break
        else: # if user's answer is wrong goes to here, 
            chance -= 1 # user will lost one chance
            if chance > 0: # if user still have chance, loop continue
                print "\nIncorrect! Please try again! " + \
                str(chance) + " chance left!"
            else: # if user ran out of chance, game over
                print "\nGame Over!"
                break
    

play_game(select_level())