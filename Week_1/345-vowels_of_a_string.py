class Solution:
    """
    This solution is not very space efficient. Time complexity could also be improved.
    """
    def reverseVowels(self, s: str) -> str:
        ind_list = []
        
        # keep an index list of all vowels
        for i, l in enumerate(s):
            if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or \
            l == 'A' or l == 'E' or l == 'I' or l == 'O' or l == 'U':
                ind_list.append(i)
                
        s = list(s)
                
        len_ind_list = len(ind_list)
        mid_ind_list = len_ind_list // 2
        
        #use the index list of vowels to flip locations in s
        for i in range(len_ind_list):
            if i < mid_ind_list:
                temp = s[ind_list[i]]
                s[ind_list[i]] = s[ind_list[len_ind_list - 1 - i]]
                s[ind_list[len_ind_list - 1 - i]] = temp
                
        return ''.join(s)
