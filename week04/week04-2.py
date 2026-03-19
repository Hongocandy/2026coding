#week04-2.py 1732.
#找到最高的海拔高度(一直加就好)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N=len(gain) #陣列的長度N
        ans=H=0 #一開始的高度是0
        #答案一開始是0 因為一開始的高度是0
        for i in range(N): #逐個加起來
            H+=gain[i] #現在增減的量gain[i] 加進H
            ans=max(ans,H) #更新最高的答案
        return ans