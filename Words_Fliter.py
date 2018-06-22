class WordsFliter(object):
    def getWords(self):
        words_bank=[]
        with open("SensitiveWords.txt") as words_file:
            words=words_file.readlines()
            for word in words:
                words_bank.append(word[0:-1])
        return words_bank
