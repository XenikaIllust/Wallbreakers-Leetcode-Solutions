"""
I recognized that it is important to establish a hashmap with key as ASCII of a
lowercase character and value as morse code signature. Then, a set is used because 
it does not have repeating elements. Thus, I could simply return the length of the
set because it contains only unique morse codes.
"""

from collections import Counter

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_alphabets = [".-","-...","-.-.","-..",".","..-.","--.","....",\
                           "..",".---","-.-",".-..","--","-.","---",".--.",\
                           "--.-",".-.","...","-","..-","...-",".--","-..-",\
                           "-.--","--.."]
        words_dict = dict(zip([ord('a') + i for i in range(len(morse_alphabets))],\
                              morse_alphabets))
        
        
        codes_set = set()
        for word in words:
            morse_code = ""
            
            for l in word:
                morse_code += words_dict[ord(l)]
                
            codes_set.add(morse_code)
            
        return len(codes_set)
