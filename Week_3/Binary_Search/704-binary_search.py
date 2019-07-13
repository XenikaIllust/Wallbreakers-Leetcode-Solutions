"""
Fairly straightforward implementation of Binary Search Tree. Only issue is Python does pass-by-assignment, so I put the target index in a mutable object so I could pass it by reference.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        class TreeNode:
            def __init__(self, val, ind):
                self.left = None
                self.right = None
                self.val = val
                self.index = ind
                
        def buildBalancedTree(nums, start, end):
            if start == end:
                return None
            
            mid = (end - start) // 2 + start
            
            root = TreeNode(nums[mid], mid)
            root.left = buildBalancedTree(nums, start, mid)
            root.right = buildBalancedTree(nums, mid + 1, end)
            
            return root
        
        def binarySearch(target, target_ind, root):
            if root == None:
                return
            
            if root.val == target:
                target_ind[0] = root.index
                return
            
            binarySearch(target, target_ind, root.left)
            binarySearch(target, target_ind, root.right)
            
            return
        
        root = buildBalancedTree(nums, 0, len(nums))
        
        target_ind = [None]
        binarySearch(target, target_ind, root)
        
        if target_ind[0] != None:
            return target_ind[0]
        else:
            return -1
