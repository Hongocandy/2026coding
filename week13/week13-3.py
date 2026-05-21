#week13-3.py 215.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #先用錯誤的寫法示範一次
        #nums.sort(reverseTrue) #先大到小排好
        #return nums[k-1] #第k大的數 是0...k-1

        #藥用Heap 資料結構 可以找出最小的數
        #heapify(nums) #變成heap資料結構
        #while nums:
        #      print(heappop(nums))

        #最後用這個版本
        heapify(nums) #變成heap資料結構0(logN)
        for i in range(len(nums)-k):
            heappop(nums) #吐掉不用的 N-k 個數
        return heappop(nums) #剩下的那個 就是第k大的