"""
This question is spiritually similar to the isomorphic strings problem. I used the same approach, by forming two
signature strings and comparing them for integrity.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_sig_dict = {}
        
        pattern_sig = ""
        type_cnt = 0
        for l in pattern:
            if l not in pattern_sig_dict:
                pattern_sig_dict[l] = str(type_cnt)
                type_cnt += 1
            pattern_sig += pattern_sig_dict[l]
            
        s = s.split(" ")
        
        s_sig_dict = {}
        
        s_sig = ""
        type_cnt = 0
        for word in s:
            if word not in s_sig_dict:
                s_sig_dict[word] = str(type_cnt)
                type_cnt += 1
            s_sig += s_sig_dict[word]
            
        if s_sig == pattern_sig:
            return True
        
        return False
