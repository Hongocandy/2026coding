#week10-5.py 437.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter=Counter()
        counter[0]=1 #有1個上帝視角的0
        def helper(root,total): #之前的total
            if root==None:return 0
            total+=root.val
            counter[total]+=1 #累積多一個total(的斷點)
            ans=counter[total-targetSum]
            ans+=helper(root.left,total)
            ans+=helper(root.right,total)
            counter[total]-=1 #再扣掉
            return ans
        return helper(root,0)
        