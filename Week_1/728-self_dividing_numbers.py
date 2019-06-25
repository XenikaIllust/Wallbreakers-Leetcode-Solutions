class Solution:
    """
    As this question can be a little messy if not organized properly, I wanted to think
    in a very organized way, hence I broke the "simple" functions down into self-defined
    functions.
    """
    
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # This function extracts a digit from a number and divides the number by 10
        def extract_digit(num):
            target = num % 10
            num //= 10
            return target, num
        
        # This function checks if a number is 0 (used for digits)
        def check_zero(num):
            if num == 0:
                return True
            else:
                return False
            
        # This function checks if a number is divisible by a target
        def check_divisible(num, target):
            if num % target == 0:
                return True
            else:
                return False
            
        sd_list = []
        
        for i in range(left, right + 1):
            zero_status = False
            divisible_status = False
            
            # Made a copy of i as i will be modified in the process
            i_cpy = i
            
            while i != 0:
                target, i = extract_digit(i)
                zero_status = check_zero(target)
                if zero_status == True:
                    break
                    
                divisible_status = check_divisible(i_cpy, target)
                if divisible_status == False:
                    break
                    
            if zero_status == True or divisible_status == False:
                pass
            else:
                sd_list.append(i_cpy)
                
        return sd_list
