

def randomAlphaNumeric( length ):
    alphaNumeric = ''
    for i in range(0, length):
        alphaNumeric = alphaNumeric + random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return alphaNumeric

def getRandomQuote():
    quotes = ['There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.\r\n', \
		'Many were increasingly of the opinion that they\'d all made a big mistake in coming down from the trees in the first place. And some said that even the trees had been a bad move, and that no one should ever have left the oceans.\r\n', \
		'\"My doctor says that I have a malformed public-duty gland and a natural deficiency in moral fibre,\" Ford muttered to himself, \"and that I am therefore excused from saving Universes.\"\r\n', \
		'The ships hung in the sky in much the same way that bricks don\'t.\r\n', \
		'\"You know,\" said Arthur, \"it\'s at times like this, when I\'m trapped in a Vogon airlock with a man from Betelgeuse, and about to die of asphyxiation in deep space that I really wish I\'d listened to what my mother told me when I was young.\"\r\n\"Why, what did she tell you?\"\r\n\"I don\'t know, I didn\'t listen.\"\r\n', \
		'\"Space,\" it says, \"is big. Really big. You just won\'t believe how vastly, hugely, mindbogglingly big it is. I mean, you may think it\'s a long way down the road to the chemist\'s, but that\'s just peanuts to space.\"\r\n', \
		'\"Funny,\" he intoned funereally, \"how just when you think life can\'t possibly get any worse it suddenly does.\"\r\n', \
		'Isn\'t it enough to see that a garden is beautiful without having to believe that there are fairies at the bottom of it too?\r\n', \
		'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.\r\n', \
		'Curiously enough, the only thing that went through the mind of the bowl of petunias as it fell was Oh no, not again. Many people have speculated that if we knew exactly why the bowl of petunias had thought that we would know a lot more about the nature of the Universe than we do now.\r\n', \
		'The reason why it was published in the form of a micro sub meson electronic component is that if it were printed in normal book form, an interstellar hitchhiker would require several inconveniently large buildings to carry it around in.\r\n', \
		'For instance, on the planet Earth, man had always assumed that he was more intelligent than dolphins because he had achieved so much - the wheel, New York, wars and so on - whilst all the dolphins had ever done was muck about in the water having a good time. But conversely, the dolphins had always believed that they were far more intelligent than man - for precisely the same reasons.\r\n', \
		'The last ever dolphin message was misinterpreted as a surprisingly sophisticated attempt to do a double-backwards-somersault through a hoop whilst whistling the \'Star Spangled Banner\', but in fact the message was this: So long and thanks for all the fish.\r\n', \
		'The chances of finding out what\'s really going on in the universe are so remote, the only thing to do is hang the sense of it and keep yourself occupied.\r\n', \
		'\"Listen, three eyes,\" he said, \"don\'t you try to outweird me, I get stranger things than you free with my breakfast cereal.\"\r\n', \
		'\"Forty-two,\" said Deep Thought, with infinite majesty and calm.\r\n', \
		'Not unnaturally, many elevators imbued with intelligence and precognition became terribly frustrated with the mindless business of going up and down, up and down, experimented briefly with the notion of going sideways, as a sort of existential protest, demanded participation in the decision-making process and finally took to squatting in basements sulking.\r\n', \
		'The Total Perspective Vortex derives its picture of the whole Universe on the principle of extrapolated matter analyses.To explain - since every piece of matter in the Universe is in some way affected by every other piece of matter in the Universe, it is in theory possible to extrapolate the whole of creation - every sun, every planet, their orbits, their composition and their economic and social history from, say, one small piece of fairy cake. The man who invented the Total Perspective Vortex did so basically in order to annoy his wife.\r\n', \
		'\"Shee, you guys are so unhip it\'s a wonder your bums don\'t fall off.\"\r\n', \
		'It is known that there are an infinite number of worlds, simply because there is an infinite amount of space for them to be in. However, not every one of them is inhabited. Therefore, there must be a finite number of inhabited worlds. Any finite number divided by infinity is as near to nothing as makes no odds, so the average population of all the planets in the Universe can be said to be zero. From this it follows that the population of the whole Universe is also zero, and that any people you may meet from time to time are merely the products of a deranged imagination.\r\n', \
		'The disadvantages involved in pulling lots of black sticky slime from out of the ground where it had been safely hidden out of harm\'s way, turning it into tar to cover the land with, smoke to fill the air with and pouring the rest into the sea, all seemed to outweigh the advantages of being able to get more quickly from one place to another.\r\n', \
		'Make it totally clear that this gun has a right end and a wrong end. Make it totally clear to anyone standing at the wrong end that things are going badly for them. If that means sticking all sort of spikes and prongs and blackened bits all over it then so be it. This is not a gun for hanging over the fireplace or sticking in the umbrella stand, it is a gun for going out and making people miserable with.\r\n', \
		'It is a well known fact that those people who most want to rule people are, ipso facto, those least suited to do it. To summarize the summary: anyone who is capable of getting themselves made President should on no account be allowed to do the job.\r\n', \
		'\"Since we decided a few weeks ago to adopt the leaf as legal tender, we have, of course, all become immensely rich.\"\r\n', \
		'In the end, it was the Sunday afternoons he couldn\'t cope with, and that terrible listlessness that starts to set in about 2:55, when you know you\'ve taken all the baths that you can usefully take that day, that however hard you stare at any given paragraph in the newspaper you will never actually read it, or use the revolutionary new pruning technique it describes, and that as you stare at the clock the hands will move relentlessly on to four o\'clock, and you will enter the long dark teatime of the soul.\r\n', \
		'He gazed keenly into the distance and looked as if he would quite like the wind to blow his hair back dramatically at that point, but the wind was busy fooling around with some leaves a little way off.\r\n', \
		'\"He was staring at the instruments with the air of one who is trying to convert Fahrenheit to centigrade in his head while his house is burning down.\"',
		'There is a moment in every dawn when light floats, there is the possibility of magic. Creation holds its breath.\r\n', \
		'\"You may not instantly see why I bring the subject up, but that is because my mind works so phenomenally fast, and I am at a rough estimate thirty billion times more intelligent than you. Let me give you an example. Think of a number, any number.\"\r\n\"Er, five,\" said the mattress. \r\n\"Wrong,\" said Marvin. \"You see?\"\r\n', \
		'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.\r\n', \
		'It is a mistake to think you can solve any major problems just with potatoes.\r\n', \
		'He hoped and prayed that there wasn\'t an afterlife. Then he realized there was a contradiction involved here and merely hoped that there wasn\'t an afterlife.\r\n', \
		'Eskimos had over two hundred different words for snow, without which their conversation would probably have got very monotonous. So they would distinguish between thin snow and thick snow, light snow and heavy snow, sludgy snow, brittle snow, snow that came in flurries, snow that came in drifts, snow that came in on the bottom of your neighbor\'s boots all over your nice clean igloo floor, the snows of winter, the snows of spring, the snows you remember from your childhood that were so much better than any of your modern snow, fine snow, feathery snow, hill snow, valley snow, snow that falls in the morning, snow that falls at night, snow that falls all of a sudden just when you were going out fishing, and snow that despite all your efforts to train them, the huskies have pissed on.\r\n', \
		'The storm had now definitely abated, and what thunder there was now grumbled over more distant hills, like a man saying \"And another thing...\" twenty minutes after admitting he\'s lost the argument.\r\n', \
		'He was wrong to think he could now forget that the big, hard, oily, dirty, rainbow-hung Earth on which he lived was a microscopic dot on a microscopic dot lost in the unimaginable infinity of the Universe.\r\n', \
		'\"It seemed to me,\" said Wonko the Sane, \"that any civilization that had so far lost its head as to need to include a set of detailed instructions for use in a packet of toothpicks, was no longer a civilization in which I could live and stay sane.\"\r\n', \
		'\"Nothing travels faster than the speed of light with the possible exception of bad news, which obeys its own special laws.\"\r\n', \
		'The last time anybody made a list of the top hundred character attributes of New Yorkers, common sense snuck in at number 79.\r\n', \
		'Protect me from knowing what I don\'t need to know. Protect me from even knowing that there are things to know that I don\'t know. Protect me from knowing that I decided not to know about the things that I decided not to know about. Amen.\r\n', \
		'All you really need to know for the moment is that the universe is a lot more complicated than you might think, even if you start from a position of thinking it\'s pretty damn complicated in the first place.\r\n', \
		'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.\r\n', \
		'Don\'t Panic.\r\n', \
		'Quite possibly, I am the best thing since sliced bread. -TJW\r\n']
    return random.choice(quotes)

def addQuoteToFile( fullFilePath ):
	textFile = open(fullFilePath, 'a')
	textFile.write(getRandomQuote())
	textFile.close()

def main():
    # First, create variables to hold parameter values when accepted
    boolHelp = False
    strScrambleText = None
    boolAboutChecked = False
    boolQuoteChecked = False
    strConstellationValue = None
    intRandomCharacterLength = -1
    strFilename = None

    i = 1
    while i < len(sys.argv):
        if (sys.argv[i] == '-help') or (sys.argv[i] == '/?'):
            boolHelp = True
        elif sys.argv[i] == '-about':
            boolAboutChecked = True
        elif sys.argv[i] == '-quote':
            boolQuoteChecked = True
            if i+1 < len(sys.argv):
                if (sys.argv[i+1][i] != '-'):
                    # The next value is a value, not another parameter
                    strFilename = sys.argv[i+1]
                    i += 1
        elif sys.argv[i] == '-scramble':
            if i+1 < len(sys.argv):
                if sys.argv[i+1][0] != '-':
                    strScrambleText = sys.argv[i+1]
                    i += 1
                else:
                    print 'Value for the -scramble parameter is missing'
                    break
        elif sys.argv[i] == '-constellation':
            if i+1 < len(sys.argv):
                if sys.argv[i+1][0] != '-':
                    strConstellationValue = sys.argv[i+1]
                    i += 1
                else:
                    print 'Value for the -constellation parameter is missing'
                    break
        elif sys.argv[i] == '-random':
            if i+1 < len(sys.argv):
                if sys.argv[i+1][0] != '-':
                    intRandomCharacterLength = int(sys.argv[i+1])
                    i += 1
                else:
                    print 'Value for the -random parameter is missing'
                    break
        i += 1
    if boolHelp:
        print 'These are the common commands for IICL:'
        print '  -about               Gives information about IICL and credits'
        print '  -quote "file.txt"    Appends one Douglas Adams quote to the text file followed by two returns.'
        print '  -constellation [X]   Accepts orion, ursaminor, aries, and virgo'
        print '  -random X            Produces X number of random charachters max of 11'
        print '  -scramble "asdf"     Scrambles the text entered into a random order'
        print '  -quote               Echoes back one Douglas Adams Quote'
        print '  -help                Shows this message'
        print '  /?                   Shows this message'
    # Do your validation here. Check with "var is None" for string variables or " < 0" for integer values
    else:
        pass #do whatever method is asked
        if boolAboutChecked:
            print 'ABOUT TEXT GOES HERE.'
        if strFilename:
            'quote: ' + str(boolQuoteChecked) + ', ' + strFilename
        else:
            'quote: ' + str(boolQuoteChecked) + ', None'
        if strConstellationValue:
            print 'CONSTELLATION GOES HERE. YOU REQUESTED: ' + strConstellationValue + '.'
        if intRandomCharacterLength > -1:
            print 'DO RANDOM CHARACTERS CODE HERE. YOU REQUESTED: ' + str(intRandomCharacterLength) + ' RANDOM CHARACTERS.'
            print randomAlphaNumeric(intRandomCharacterLength)
        if strScrambleText:
            print 'DO TEXT SCRAMBLING HERE.'
            print strScrambleText

    #for i, arg in enumerate(sys.argv):
    #    if arg == '-about':
    #        print 'The Infinite Improbability Command Line is a command line interface (CLI) that performs'
    #        print 'basic functions and is used as an example program for UGUI to create a GUI for.'
    #        print 'IICL is created in Python by Hai Nguyen.'
    #    if arg == '-random':
    #        print randomAlphaNumeric(int(sys.argv[i + 1]))
    #    if arg == '-quote':
    #        addQuoteToFile(sys.argv[i + 1])
    sys.exit()

if __name__ == '__main__':
    import sys
    import os
    import random
    main()