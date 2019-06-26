class Solution:
    def reverseWords(self, s: str) -> str:
        """
        My solution only beat 5.53% of submissions and is quite slow. I would like to know
        if there is a much more optimized way to solve the problem. My solution takes the
        string and breaks it up into a list by splitting at spaces. It then reverses every
        word in the words list and then joins them back.
        """
        def reverseWordInPlace(word):
            len_word = len(word)
            mid_word = len_word // 2
            
            word_list = list(word)
            
            for i, letter in enumerate(word):
                if i < mid_word:
                    temp = word_list[i]
                    word_list[i] = word_list[len_word - 1 - i]
                    word_list[len_word - 1 - i] = temp
                    
            return ''.join(str(l) for l in word_list)
                    
        words_list = s.split(" ")
        
        for i, word in enumerate(words_list):
            words_list[i] = reverseWordInPlace(words_list[i])
            
        return " ".join(words_list)
