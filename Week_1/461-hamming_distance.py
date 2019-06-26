class Solution:
    """
    My solution was to convert both numbers into base 2 representation, and add leading
    zeros where necessary to make both lengths the same. Then, I found the differences
    between the bits and summed them up. I think memory usage could still be improved.
    """
    
    def hammingDistance(self, x: int, y: int) -> int:
        def convertToBaseTwo(x):
            bit_list = []
            while x != 0:
                rem = x % 2
                bit_list.insert(0, rem)
                x //= 2
                
            return bit_list
        
        x_bits = convertToBaseTwo(x)
        y_bits = convertToBaseTwo(y)
        
        if len(x_bits) > len(y_bits):
            for i in range(len(x_bits) - len(y_bits)):
                y_bits.insert(0, 0)
        elif len(y_bits) > len(x_bits):
            for i in range(len(y_bits) - len(x_bits)):
                x_bits.insert(0, 0)
               
        hamm_dist = 0
        for i in range(len(x_bits)):
            if x_bits[i] != y_bits[i]:
                hamm_dist += 1
                
        return hamm_dist
