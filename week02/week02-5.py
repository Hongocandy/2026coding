#week02-5.py 1679題
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #小到大排好 等遺下邊挑一個 右邊挑一個 看能不能組合
        i,j=0,len(nums)-1 #最左邊i最小 最右邊j對應最大的
        ans=0
        while i<j: #左右還沒有撞在一起 就可以左右各挑選
            if nums[i]+ nums[j]==k: #太好了 剛剛好 !
                ans+=1
                i,j=i+1,j-1#右邊用了 往右 右邊用了 往左
            if nums[i]+nums[j]<k: #加起來太小了 那左邊小的要往右移
                i=i+1
            if nums[i]+nums[j]>k: #加起來太大了 那右邊大的j要往左移
                j-=1
        return ans