class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        My solution finds the first two sums and then breaks. It does this by using nested
        hashmaps. The outer hashmap links a number to an inner hashmap. The inner hashmap
        keeps track of the index location and the count. The count is kept track of
        to prevent adding of single elements. For example, in [3,2,4], the 3 should
        not be added as there is only one 3 in the list.
        """
        
        num_ind_count = dict()
        
        target_indexes = []
        
        for i, n in enumerate(nums):
            if n not in num_ind_count:
                num_ind_count[n] = {"ind":[i], "count":1}
            else:
                num_ind_count[n]["ind"].append(i)
                num_ind_count[n]["count"] += 1
                
            diff = target - n
            
            if diff in num_ind_count and (diff != n or num_ind_count[diff]["count"] > 1):
                for x in num_ind_count[n]["ind"]:
                    target_indexes.append(x)
                    
                for x in num_ind_count[diff]["ind"]:
                    target_indexes.append(x)
                    
                break
                
        return list(set(target_indexes))
