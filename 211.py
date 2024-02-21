class WordDictionary:

    def __init__(self):
        self.words = set()
        self.words_with_dots = set()        

    def addWord(self, word: str) -> None:
        self.words.add(word)
        

    def search(self, word: str) -> bool:
        return True
        

if __name__ == '__main__':
    pass