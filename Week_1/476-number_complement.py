class Solution:
    def findComplement(self, num: int) -> int:
        """
        My solution breaks down a base 10 number into base 2 and flips the bits as 
        represented in a list. The flipped bits are then recombined into a base 10 number.
        """
        bit_list = []
        while num != 0:
            rem = num % 2
            if rem == 0:
                bit_list.insert(0,1)
            else:
                bit_list.insert(0,0)
                
            num //= 2
            
        len_bit_list = len(bit_list)
        sum = 0
        for i in range(len_bit_list):
            sum += bit_list[i] * (2 ** (len_bit_list - 1 - i))
            
        return sum
