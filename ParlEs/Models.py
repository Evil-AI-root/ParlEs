from collections import Counter


class BagOfWords(object):
    def __init__(self, tokens=[]):
        self.counter = Counter(tokens)
        self.only = len(self.counter.keys())

    def model(self, only=20):
        num = self.only
        if only < num:
            num = only
        output = {}
        for i in range(num):
            output[list(self.counter.keys())[i]] = 0
        return output
