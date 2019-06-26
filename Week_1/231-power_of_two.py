class Solution:
    """
    For this question, the brute force solution is extremely inefficient. I noticed that
    if a number is a power of two, it will be the the product of any smaller power of 
    two when n > 2. With this, I saved on many steps of computation. I used that to my
    advantage to quickly find the solution.
    """
    
    def isPowerOfTwo(self, n: int) -> bool:
        is_power_of_two = False
        
        i = 1
        while i <= n:
            if i * i == n or i == n:
                is_power_of_two = True
                break
                
            i *= 2
            
        return is_power_of_two
