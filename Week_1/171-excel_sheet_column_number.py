class Solution:
    """
    When I saw the relationship between the numbers, I immediately thought of using
    base 26, due to the power nature of the numbers.
    """
    
    def titleToNumber(self, s: str) -> int:
        sum = 0
        
        count = 0
        for i in range(len(s) - 1, -1, -1):
            sum += (ord(s[i]) - 64) * (26 ** count) # use 64 as it is the ASCII value of A - 1
            count += 1
            
        return sum
