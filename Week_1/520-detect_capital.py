class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        This question was super tricky. I suppose there is a better solution out there,
        but I managed to break down the problem into three cases, and wrote a different
        function to handle each case depending on which case was still true. The surviving
        case (if any) would mean the capital use is accurate.
        
        First condition: All caps
        Second condition: First caps only 
        Third condition: All small
        """
        def checkCapital(letter):
            letter_val = ord(letter)
            if letter_val >= 65 and letter_val <= 90:
                return True
            else:
                return False
            
        def checkFirst(prev_status, curr_letter):
            """
            check for capitals only
            """
            curr_status = prev_status
            
            if checkCapital(curr_letter):
                curr_status = True
            else:
                curr_status = False
            
            return curr_status
        
        def checkSecond(prev_status, ind, curr_letter):
            """
            check for capital if ind == 0, else check for smalls
            """
            curr_status = prev_status
            
            if ind == 0:
                curr_status = checkCapital(curr_letter)
            else:
                curr_status = not checkCapital(curr_letter)
            
            return curr_status
        
        def checkThird(prev_status, curr_letter):
            """
            check for smalls only
            """
            curr_status = prev_status
            
            if not checkCapital(curr_letter):
                curr_status = True
            else:
                curr_status = False
            
            return curr_status
        
        if len(word) == 1:
            return True
        
        first_status = True
        second_status = True
        third_status = True
        
        for i, letter in enumerate(word):            
            if first_status:
                first_status = checkFirst(first_status, letter)
                
            if second_status:
                second_status = checkSecond(second_status, i, letter)
                
            if third_status:
                third_status = checkThird(third_status, letter)
                
        if (first_status == True and second_status == False and third_status == False) \
        or (first_status == False and second_status == True and third_status == False) \
        or (first_status == False and second_status == False and third_status == True):
            return True
        else:
            return False
