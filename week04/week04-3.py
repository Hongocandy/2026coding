#week04-3.py 3866.
#找到陣列nums裡 只出現過一次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        N=len(nums) #有N個數
        #第一種寫法 用陣列 先統計出現的次數
        H=[0]*200 #很多很多格 H[??]對應??出現幾次
        for i in range(N):
            H[nums[i]]+=1 #把出現的數字 塞進H[??]裡
        for i in range(N): #逐一檢查
            if nums[i]%2==0 and H[nums[i]]==1: #偶數才處理
               return  nums[i] #找到答案了

        return -1