import fractions, pdb, random

def simple_bet_scenario(potSize, betSize):
    """
    @param potSize: potSize including the incoming bet
    @param betSize: incoming betSize
    """
    flopDraws = {"Open Ended Straight Draw": 8, "Flush Draw": 9, "Inside Straight Draw": 4, "Trips Draw": 2, "Full House Draw (Flop)" : 7}
    print "The pot size prior to your opponents bet is", potSize
    print "The Bet Size is: ", betSize
    pOdds = raw_input("What are your pot odds\n\t")
    potSize = potSize + betSize
    trueOdds = fractions.Fraction(betSize, potSize)
    print "\tThe Correct Answer is {0}: {1}".format(trueOdds.denominator, trueOdds.numerator)
    your_position =  random.choice(flopDraws.keys())
    decision = raw_input("With a {0} on the flop, should you call?\n\t".format(your_position))
    outs = flopDraws[your_position]

    #flop odds estimator
    if outs > 8:
        approx_win_prob = outs * 4 - (outs  - 8) 
    else:
        approx_win_prob = outs * 4 
    approx_odds = fractions.Fraction(approx_win_prob, 100 - approx_win_prob)
    prob_thresh = 1.*betSize / (potSize + betSize)
    shouldCall = approx_win_prob / 100. > prob_thresh 
    if shouldCall:
        print "You should call!"
    print "\tYou have {0} outs, making the probability of winning, {1}%, and your odds \n\t\t{2} : {3} or".\
            format(outs, approx_win_prob, approx_odds.denominator, approx_odds.numerator)
    print "\t\t{0}: {1}".format(1.*trueOdds.numerator * approx_odds.denominator / approx_odds.numerator, trueOdds.numerator)

    if (shouldCall and decision[0] == 'y') or (not shouldCall and decision[0] != 'y'):
        print "You got it right"
        return True
    print "\tYou need at least {0}/{1} or {2:.2f}% equity in order to call".format(betSize, potSize, prob_thresh*100)
    print "Whoops, you made a mistake"
    return False

def simulate_flops(nSims=10):
    wrong = 0
    potSizes = range(50, 320, 5)
    betFracs = range(1,9) + [.25, .5]*4
    for i in range(nSims):
        potSize = random.choice(potSizes)
        betFraction = random.choice(betFracs)
        if not simple_bet_scenario(potSize, int(potSize/ betFraction)/10*10):
            wrong += 1
        print '--'*30
    print "You got {0} out of {1} right".format(nSims - wrong, nSims)
simulate_flops()
