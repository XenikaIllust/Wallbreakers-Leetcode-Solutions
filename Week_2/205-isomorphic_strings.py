"""
If two strings are isomorphic, I can give every new letter type a signature. For example, "egg" -> "0.1.1."
and "add" -> "0.1.1.". A full stop is added to each letter signature to distinguish a digit. If two strings
are not isomorphic, their string signature will be different. Eg, "egga" -> "0.1.1.2." and "aded" -> "0.1.2.1.".
"""

from collections import OrderedDict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        comparator_s = ""
        comparator_t = ""
        
        s_letter_id_dict = OrderedDict()
        
        type_cnt = 0
        for l in s:
            if l not in s_letter_id_dict:
                s_letter_id_dict[l] = str(type_cnt)
                type_cnt += 1
            comparator_s += s_letter_id_dict[l]
            comparator_s += "."
            
        t_letter_id_dict = OrderedDict()
        
        type_cnt = 0
        for l in t:
            if l not in t_letter_id_dict:
                t_letter_id_dict[l] = str(type_cnt)
                type_cnt += 1
            comparator_t += t_letter_id_dict[l]
            comparator_t += "."
            
        if comparator_s == comparator_t:
            return True
        
        return False
