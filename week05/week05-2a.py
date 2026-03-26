#week05-2a.py 2215.
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1=[]#放 在nums1 但不在nums2的數
        for num in nums1: #逐一取出
            if num not in nums2: #沒在裡面
                ans1.append(num) #放入答案
        ans2=[] #放 在nums2但不再nums1的數
        for num in nums2:
            if num not in nums1:
                ans2.append(num)
        return [list(set(ans1)),list(set(ans2))] #把芳括號list變set 在變回list 重複地就不見了