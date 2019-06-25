class Solution:
    """
    This question is very tricky due to the edge case, when a number is 999...9.
    Therefore, a carry flag must be established so that, after iterating through all digits,
    should there still be a carry, a one will be inserted to the head of the list.
    """
    
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1 

            if digits[i] == 10:
                digits[i] = 0
                carry = True
            else:
                carry = False
                break
                
        if carry == True:
            digits.insert(0, 1)
            
        return digits
