import fractions, pdb, random

def approx_pot_odds(potSize, betSize):
    """
    @param potSize: potSize including the incoming bet
    @param betSize: incoming betSize
    """
    flopDraws = {"Open Ended Straight Draw": 8, "Flush Draw": 9, "Inside Straight Draw": 4, "Trips Draw": 2, "Full House Draw (Flop)" : 7}

    print "The Bet Size is: ", betSize
    print "Making the total potSize: ", potSize
    pOdds = raw_input("What are your pot odds\n\t")
    trueOdds = fractions.Fraction(betSize, potSize)
    print "\tThe Correct Answer is {0}: {1}".format(trueOdds.denominator, trueOdds.numerator)
    your_position =  random.choice(flopDraws.keys())
    decision = raw_input("With a {0} on the flop, should you call?\n\t".format(your_position))
    outs = flopDraws[your_position]
    if outs > 8:
        approx = outs * 4 - (outs  - 8) 
    else:
        approx = outs * 4 
    approx_odds = fractions.Fraction(approx, 100)
    prob_thresh = 1.*betSize/potSize
    shouldCall = prob_thresh> approx / 100. 
    print "\tYou have {0} outs, making the probability of winning and your odds {1}%, {2} : {3}".format(outs, approx, approx_odds.denominator, approx_odds.numerator)
    print "\t You need at least {0}% equity in order to call".format(prob_thresh*100)
    if (shouldCall and decision == 'y') or (shouldCall and decision != 'y'):
        print "You got it right"
    else:
        print "Whoops, you made a mistake"



approx_pot_odds(100, 30)
