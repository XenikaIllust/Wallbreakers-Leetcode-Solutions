from collections import defaultdict

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.next = defaultdict(lambda: None)
        self.tail = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        curr = self.root
        
        for i,l in enumerate(word):
            if curr.next[l] == None:
                curr.next[l] = TrieNode(l)
                
            if i == len(word) - 1:
                curr.next[l].tail = True
                    
            curr = curr.next[l]
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        curr = self.root
        
        for i,l in enumerate(word):
            if curr.next[l] == None:
                return False
            if i == len(word) - 1 and curr.next[l].tail == False:
                return False
            
            curr = curr.next[l]
            
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        curr = self.root
        
        for i,l in enumerate(prefix):
            if curr.next[l] == None:
                return False
            
            curr = curr.next[l]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
