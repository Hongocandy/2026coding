#week04-5.py 724.
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N=len(nums) #陣列的長度N
        prefix = [0] #一開始prefix sum只有1個[0]
        for i in range(N):
            prefix.append(prefix[-1]+nums[i])#陣列變長了
        #debug印出來看一下
        #print(prefix)
        postfix=[0]*(N+1)
        for i in range(N-1,-1,-1): #倒過來的迴圈
            postfix[i]=postfix[i+1]+nums[i]
        for i in range(N):
            if prefix[i]==postfix[i+1]:return i
        return -1