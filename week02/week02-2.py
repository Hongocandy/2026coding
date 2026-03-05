class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        N=len(nums) #陣列大小
        k=0 #要宣告k一開始要在最左邊待命
        for i in range(N): #把nums[i]逐一檢查
            if nums[i]!=0: #遇到不是0的數 要搬到左邊
                nums[k]=nums[i]#左邊nums[k] 右邊nums[i]
                k+=1 #k換下一個位置
        for i in range(k,N): #剩下的格子
            nums[i]=0 #全部補0