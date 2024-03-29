import math
import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number==0:
        return "rock"
    elif number==1:
        return "Spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissors"
    else:
        return "cannot convert number to name"
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name=='rock':
        return 0
    elif name=='Spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        return "do not match"
    
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below
    # convert name to player_number using name_to_number
    player_number=name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randint(0,4)
    # compute difference of player_number and comp_number modulo five
    diff=player_number-comp_number
    if diff<0:
        diff=5+diff
    # use if/elif/else to determine winner
    print player_number
    print comp_number
    print diff
    print "Player choose " + number_to_name(player_number)
    print "Computer choose " + number_to_name(comp_number)
    if diff==1 or diff==2:      
        print "Player wins!\n"
    elif diff==3 or diff==4:      
        print "Computer wins!\n"  
    else:
        print "Player and computer tie!\n"  
    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

