class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        My strategy for this was to keep an array of all lengths of strings so that
        I could terminate at the minimum string's length. I have a prefix that gets 
        appended if all the current letters in that position for every string is the
        same. Otherwise, the program returns the last known prefix.
        """
        
        prefix = ""
        
        target = ""
        
        if len(strs) == 0:
            return prefix
        
        lens = []
        for i in range(len(strs)):
            lens.append(len(strs[i]))
        
        for j in range(min(lens)):
            for i in range(len(strs)):
                curr_l = strs[i][j]

                if target == "" or i == 0:
                    target = curr_l

                if curr_l != target:
                    return prefix

            prefix += target
            
        return prefix
