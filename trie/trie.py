class Trie:
    def __init__(self) -> None:
        self.root = TrieNode('', False)
        
    def insert(self, word: str) -> None:
        iteration = 1
        current_node: TrieNode = self.root
        for char in word:
            if char in current_node.children:
                current_node = current_node.children[char]
                iteration += 1
            else:
                if len(word) == iteration:
                    new_node: TrieNode = TrieNode(char, True)
                else:
                    new_node: TrieNode = TrieNode(char, False)
                
                iteration += 1
                current_node.children[char] = new_node
                current_node = new_node
    
    def traverse(self) -> None:
        self._dfs(self.root, '')
    
    def _dfs(self, node: TrieNode, chars_so_far: str) -> None:
        if node:
            if node.is_end_of_word:
                print(chars_so_far + node.char)
            
            for child_node in node.children.values():
                self._dfs(child_node, chars_so_far + node.char)


class TrieNode:
    def __init__(self, char: str, is_end_of_word: bool) -> None:
        self.char: str = char
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = is_end_of_word


if __name__ == '__main__':
    trie: Trie = Trie()
    trie.insert('apple')
    trie.insert('boy')
    trie.insert('cat')

    trie.traverse()