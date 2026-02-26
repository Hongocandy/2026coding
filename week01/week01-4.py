#week01-4.py
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[] #答案的True和False 將塞在裡面
        best = max(candies) #目前小朋友 最多有幾個糖
        for candie in candies: #逐一檢查 如果把extraCandies 給小朋友
           if candie + extraCandies>=best: ans.append(True)
           else:ans.append(False) #他會不會>=最多的 依序塞入ans
        return ans