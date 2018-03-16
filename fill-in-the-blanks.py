easy_answer = ["function", "object", "wrapper", "global"]
medium_answer = ["while", "true", "false", "else"]
hard_answer = ["compound", "list", "square", "same"]

easy_question = "A ___1___ definition is an executable statement. Its execution binds the ___1___ name in the current local namespace to a ___1___ ___2___ (a ___3___ around the executable code for the ___1___). This ___1___ ___2___ contains a reference to the current ___4___ namespace as the ___4___ namespace to be used when the ___1___ is called."
medium_question = "The ___1___ statement is used for repeated execution as long as an expression is ___2___. This repeatedly tests the expression and, if it is ___2___, executes the first suite; if the expression is ___3___ (which may be the first time it is tested) the suite of the ___4___ clause, if present, is executed and the loop terminates."
hard_question = "Python knows a number of ___1___ data types, used to group together other values. The most versatile is the ___2___, which can be written as a ___3___ of comma-separated values (items) between ___3___ brackets. ___2___s might contain items of different types, but usually the items all have the ___4___ type."

blank = ["___1___", "___2___", "___3___", "___4___"]

def prompt (selected_question):
    print "\nYou will get 5 guesses per problem."
    print "\nThe current paragraph reads as such:"
    print selected_question

#ask player to choose dificulty level
def select_level ():
    user_input = raw_input("Please choose difficulty level by typing it in: easy, medium, or hard.")
    if user_input == "easy":
        return easy_answer, easy_question
    elif user_input == "medium":
        return medium_answer, medium_question
    elif user_input == "hard":
        return hard_answer, hard_question
    else:
        print "Sorry, your input is not valid!"
        return select_level()

# chack player's answer, return true or keep looping
# once reach max attempt return false
def user_attempt (standard_answer, user_attempt_answer):
    if standard_answer == user_attempt_answer:
        return True
    else:
        play_game_count = 1
        max_play_count = 5
        while play_game_count < max_play_count:
            user_attempt_answer = raw_input("That isn't the correct answer!  Let's try again; you have " + str(max_play_count - play_game_count) + " try(s) left!")
            if standard_answer != user_attempt_answer:
                play_game_count += 1
            else:
                return True
        return False


def play_game():
    answers, question = select_level() #see select_level helper function
    prompt(question) #see prompt helper function
    for element in blank: #loop over blank list
        attempt_answer = raw_input("What should be substituted in for " + element + "?")
        index = blank.index(element) #blank has same length as answers, define variable answer 
        answer = answers[index]
        if user_attempt(answer, attempt_answer) == True: #use helper function to check player's input
            question = question.replace(element, answer) #if player's input correct replace the blank space
            print "\nCorrect!"
            print "\nThe current paragraph reads as such:"
            print question
        else:
            return "\nGame Over!" #player's attempt over 5 times, game over
    return "\nYou Win!"
        
print play_game()