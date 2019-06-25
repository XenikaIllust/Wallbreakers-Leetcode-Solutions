class Solution:
    """
    For this question, two checks should be made for every number from 1 to n, a check for 
    multiples of 3 and a check for multiples of 5. If the number is not a multiple of
    either, then just print the number in str form. Otherwise, create a new str and append
    "Fizz" and/or "Buzz" depending on which multiple it is.
    """
    
    def fizzBuzz(self, n: int) -> List[str]:
        def check_divisible_three(num):
            if num % 3 == 0:
                return True
            else:
                return False
            
        def check_divisible_five(num):
            if num % 5 == 0:
                return True
            else:
                return False
        
        res = []
        
        for i in range(1, n + 1):
            three_status = check_divisible_three(i)
            five_status = check_divisible_five(i)
            
            if three_status == False and five_status == False:
                res.append(str(i))
                continue
            
            s = ""
            
            if three_status == True:
                s += "Fizz"
                
            if five_status == True:
                s += "Buzz"
                
            res.append(s)
            
        return res
