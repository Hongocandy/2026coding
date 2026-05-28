#week14-2b.py 1137.
class Solution:
    def tribonacci(self, n: int) -> int:
        a=[0,1,1]
        @cache #函式呼叫函式(不要重複問答案)
        def helper(i):
            if i<3:return a[i]
            #if i==0:return 0
            #if i==1:return 1
            #if i==2:return 1
            return helper(i-1)+helper(i-2)+helper(i-3)
        return helper(n)