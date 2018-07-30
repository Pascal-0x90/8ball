import random

class eightball(object):

    #    To use module, just run the command with whatever question.
    #    Say this is from some input such as 'input("Ask your question')
    #    and the response is 'who am i' then pass nothing and this will
    #    respond with one of the answers based on the randomint class
    def shake(self):
        decisions = ['Signs point to yes', 'Yes', 'Reply hazy, try again', 'Without a doubt', 'My sources say no',
                     'As I see it, yes', 'You may rely on it', 'Concentrate and ask again', 'Outlook not so good',
                     'It is decidedly so', 'Better not tell you now', 'Very doubtful', 'Yes - definitely',
                     'It is certain', 'Cannot predict now', 'Most likely.', 'Ask again later', 'My reply is no',
                     'Outlook good', "Don't count on it", 'Yes, in due time', 'My sources say no']
        number = random.randint(0, len(decisions))
        return decisions[number]