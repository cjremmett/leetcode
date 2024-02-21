class WordDictionary:

    def __init__(self):
        self.words = set()
        self.words_with_dots = set()        

    def addWord(self, word: str) -> None:
        self.words.add(word)
        for i in range(0, len(word)):
            for j in range(0, len(word)):
                word_with_dots = word
                word_with_dots = word_with_dots[0:i] + '.' + word_with_dots[i+1:]
                word_with_dots = word_with_dots[0:j] + '.' + word_with_dots[j+1:]
                self.words_with_dots.add(word_with_dots)

    def search(self, word: str) -> bool:
        if word in self.words or word in self.words_with_dots:
            return True
        else:
            return False
        

if __name__ == '__main__':
    trie = WordDictionary()
    trie.addWord('apple')
    print(trie.search('apple'))
    print(trie.search('ap..e'))
    print(trie.search('ap.l.'))
    print(trie.search('appledfdfds'))
    print(trie.search('a..'))