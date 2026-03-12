#week03-1.py 643.
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N=len(nums) #陣列的長度
        total=sum(nums[:k]) #加總 [:k] 前k項加起來
        maxTotal=total 
        for i in range(k,N): #右邊的頭
            total = total + nums[i]-nums[i-k]
            #nums[i]右邊的頭往右吃 nums[i-k]左邊的尾巴負責吐出
            maxTotal=max(maxTotal,total) #找到更新 找到最大的total
        return maxTotal/k #最大的平均=最大的total/k
        