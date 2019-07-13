"""
All powers can be broken down into two more digits, which are (n/2) + (n/2) if even and (n/2) + (n/2 + 1) if odd. Using this, 
memoization can be used where powers that have been previously computed can be memoized in a dictionary for maximum efficiency. 
"""

from collections import defaultdict

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        def powRec(n, powers):
            if n == 0:
                return powers[0]
            if n == 1:
                return powers[1]
            
            status = n % 2  # check for even or odd
            
            print(powers)
            
            # todo: edit this section
            if status:
                if powers[n] == None:
                    powers[n] = powRec(n // 2, powers) * powRec((n // 2) + 1, powers)
                return powers[n]
            else:
                if powers[n] == None:
                    powers[n] = powRec(n // 2, powers) * powRec((n // 2), powers)
                return powers[n]
        
        powers = defaultdict(lambda: None)
        powers[0] = 1.0
        powers[1] = x
        
        if n < 0:
            return 1 / powRec(-n, powers)
        else:
            return powRec(n, powers)
