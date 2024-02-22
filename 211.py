class WordDictionary:

    def __init__(self):
        self.words = set()        

    def addWord(self, word: str) -> None:
        self.words.add(word)                

    def search(self, word: str) -> bool:    
        period_locations = []
        for i in range(0, len(word)):
            if word[i] == '.':
                period_locations.append(i)

        if len(period_locations) == 0:
            if word in self.words:
                return True
            else:
                return False
        elif len(period_locations) == 1:
            for i in range(97, 123):
                if word.replace('.', chr(i)) in self.words:
                    return True
                
            return False
        else:
            for i in range(97, 123):
                for j in range(97, 123):
                    test_word = word[0:period_locations[0]] + chr(i) + word[period_locations[0] + 1:period_locations[1]] + chr(j) + word[period_locations[1] + 1:]
                    if test_word in self.words:
                        return True

            return False

if __name__ == '__main__':
    trie = WordDictionary()
    trie.addWord('apple')
    print(trie.search('ap.le'))
    print(trie.search('ap..e'))
    print(trie.search('.p.le'))
    print(trie.search('ap.l.'))
    print(trie.search('kjdsfaksjdfk..'))
    # print(trie.search('apple'))
    # print(trie.search('ap..e'))
    # print(trie.search('ap.l.'))
    # print(trie.search('appledfdfds'))
    # print(trie.search('a..'))