class Solution:
    """
    By using a dict, I am able to run at O(n). However, I would like to improve on memory.
    """
    def singleNumber(self, nums: List[int]) -> int:
        elem_dict = dict()
        
        for i in range(len(nums)):
            if nums[i] not in elem_dict:
                elem_dict[nums[i]] = 1
            else:
                elem_dict[nums[i]] += 1
                
        for key in elem_dict:
            if elem_dict[key] == 1:
                return key
