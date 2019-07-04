"""
I think that the reason my solution consumes so much time and memory is because I use multiple data structures.
My solution is to write a class where I can compare two classes based on the contents of their even and odd
dictionaries. Using that, I can store classes in a dictionary based on the the "similarity" of the class objects.
"""

from collections import Counter, OrderedDict, defaultdict

class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        class StringData():
            def __init__(self, s):
                self.s = s
                self.even = Counter()
                self.odd = Counter()
                
                for i, l in enumerate(self.s):
                    if i % 2 == 0:
                        self.even.update({l: 1})
                    else:
                        self.odd.update({l: 1})
                
            def __eq__(s1,s2):
                if len(s1.even) != len(s2.even) or len(s1.odd) != len(s2.odd):
                    return False
                
                for key in s1.even:
                    if key not in s2.even or s2.even[key] != s1.even[key]:
                        return False
                    
                for key in s1.odd:
                    if key not in s2.odd or s2.odd[key] != s1.odd[key]:
                        return False
                    
                return True
            
            def __ne__(s1,s2):
                if len(s1.even) != len(s2.even) or len(s1.odd) != len(s2.odd):
                    return True
                
                for key in s1.even:
                    if s2.even[key] != s1.even[key]:
                        return True
                    
                for key in s1.odd:
                    if s2.odd[key] != s1.odd[key]:
                        return True
                    
                return False
        
        s_datas = defaultdict(list)
        
        for s in A:
            s_data = StringData(s)

            s_datas[s].append(s_data)
            
            for key in s_datas:
                if key == s:
                    continue
                if s_datas[key][0] == s_data:
                    s_datas[key].append(s_data)
                    del s_datas[s]
                    break
            
        return len(s_datas)
