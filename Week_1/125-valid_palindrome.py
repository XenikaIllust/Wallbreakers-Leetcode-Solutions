class Solution:
    """
    The runtime is slow as it has to run through the list twice. I have an idea to run
    through the string only once, but I will need more time to revise the solution.
    
    The reason that I run through the string twice is because in the first round, I format
    the string to eliminate all useless characters before checking if it is a palindrome.
    """
    
    def isPalindrome(self, s: str) -> bool:       
        s_list = []
        
        for l in s:
            if (ord(l) >= ord('A') and ord(l) <= ord('Z')) or \
            (ord(l) >= ord('0') and ord(l) <= ord('9')):
                s_list.append(l)
            elif ord(l) >= ord('a') and ord(l) <= ord('z'):
                s_list.append(chr(ord(l) - 32)) # convert to caps for uniform processing
                
        mid_s_list = len(s_list) // 2
        
        for i in range(len(s_list)):
            if i < mid_s_list:
                if s_list[i] != s_list[len(s_list) - 1 - i]:
                    return False
            
        return True
