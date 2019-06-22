class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # This solution runs in O(n) time complexity. I think (for now) the only solution is O(n) because the program has to run through each element in the array. The numerical order does not matter. Therefore I created two bins called "even" and "odd" to keep elements of each category, then concatenate both. Space efficiency is O(n) because space only grows as much as # of input elements.
        
        even = []
        odd = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:   #even
                even.append(A[i])
            else:               #odd
                odd.append(A[i])
                
        return even + odd
