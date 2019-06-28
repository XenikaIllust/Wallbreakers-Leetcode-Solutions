class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        My strategy is to create two hashmaps, one for s and one for t to store 
        letters and counts as key value pairs. After populating both hashmaps,
        they are checked for integrity, ie key exists and count is same for both.
        """
        
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for l in s:
            if l not in s_dict:
                s_dict[l] = 1
            else:
                s_dict[l] += 1
                
        t_dict = dict()
        for l in t:
            if l not in t_dict:
                t_dict[l] = 1
            else:
                t_dict[l] += 1
                
        for key in s_dict:
            if key not in t_dict:
                return False
            
            if t_dict[key] != s_dict[key]:
                return False
            
        return True
