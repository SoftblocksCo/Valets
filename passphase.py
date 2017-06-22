from random import SystemRandom
_random = SystemRandom()

class Passphase():
    def __init__(self, wordlist_path):
        wordlist = open(wordlist_path, 'r')
        self.words = wordlist.read().splitlines()

    def get_phrase(self, counter):
        pp = []
        for i in range(counter):
            pp.append(_random.choice(self.words))
        return pp
