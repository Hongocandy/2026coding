#week04-4c.py 3866.
#找到陣列nums裡 只出現過一次的偶數 第一次出現的位置
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H=Counter(nums) #使用進階資料結構 可以統計數量
        for nn in nums:
            if nn%2==0 and H[nn]==1:return nn
        return -1