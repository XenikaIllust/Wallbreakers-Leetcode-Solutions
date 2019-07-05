"""
My code breaks when dealing with the case ["r","kt","jtgt","j","jtg","rdwy","chkext","c","l","zo","lnp","k","jt","chke","ktui","rd","jtgtha","ch","chkex"]
"""

from collections import defaultdict, OrderedDict

class Solution:
    def longestWord(self, words: List[str]) -> str:
        class TrieNode():
            def __init__(self, letter):
                self.letter = letter
                self.next = defaultdict(lambda: None)
                self.tail = False
                
        def build_trie_from_words(words):
            root = TrieNode(None)

            for word in words:
                curr = root
                for i, l in enumerate(word):
                    if curr.next[l] == None:
                        newnode = TrieNode(l)
                        curr.next[l] = newnode
                        curr.next = defaultdict(lambda: None, sorted(curr.next.items(), \
                                                                     key=lambda item: ord(item[0]), \
                                                                     reverse=False))

                    curr = curr.next[l]

                    if i == len(word) - 1:
                        curr.tail = True
                        
            return root
        
        def find_long_word(node, string, potential_words):
                if node == None:
                    return potential_words
                
                if len(node.next) != 0 and node.letter != None and node.tail != True:
                    return potential_words
                
                if node.letter != None:
                    string += node.letter
                    
                if len(node.next) == 0:
                    potential_words.append(string)
                    return potential_words
                
                for next_letter in node.next.keys():
                    # if node.next[next_letter].tail == False:
                    #     potential_words.append(string)
                    #     return potential_words
                    
                    find_long_word(node.next[next_letter], string, potential_words)
                    
                return potential_words
        
        def find_longest_words(root):
            potential_words = []
            string = ""
            
            find_long_word(root, string, potential_words)
            return potential_words
        
        
        root = build_trie_from_words(words)
        potential_words = find_longest_words(root)
        
        pword_data = {}
        max_len = 0
        for word in potential_words:
            if len(word) > max_len:
                max_len = len(word)
            
            lex_sum = 0
            for l in word:
                lex_sum += ord(l)
            
            pword_data[word] = len(word)
            
        pword_data_copy = pword_data.copy()
        for key in pword_data.keys():
            if pword_data_copy[key] != max_len:
                del pword_data_copy[key]
        
        return sorted(pword_data_copy.items())[0][0]
