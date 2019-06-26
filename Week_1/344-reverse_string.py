class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        """
        In this question, I perform flips, but extra care is taken to not repeat flip,
        otherwise this could result in no flip being performed. Therefore, I only flip
        if i has not passed the midpoint of the string.
        """
        
        len_s = len(s)
        mid_s = len(s) // 2
        
        for i in range(len_s):
            if i < mid_s: # prevents extra flips
                temp = s[i]
                s[i] = s[len_s - 1 - i]
                s[len_s - 1 - i] = temp
