class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False 

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word:
            i = ord(c) - ord('a') 
            if cur.children[i] is None:
                cur.children[i] = TrieNode() 
            cur = cur.children[i]
        cur.endOfWord = True 

    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                return False 
            cur = cur.children[i]
        return cur.endOfWord
                
    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] is None: 
                return False 
            cur = cur.children[i]
        return True

# Time Complexity:
# - insert(word): O(n), where n is the length of word
# - search(word): O(n), where n is the length of word
# - startsWith(prefix): O(n), where n is the length of prefix

# Space Complexity:
# - O(t), where t is the total number of TrieNodes created (depends on the inserted words and shared prefixes)
