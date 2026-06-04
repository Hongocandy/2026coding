#week15-1a.py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(i,j): #函式呼叫函式 現在若在(I,J)座標
            if i==m-1 and j==n-1:return 1 #走到終點成功
            if i==m or j==n:return 0 #走超過邊界 失敗
            return helper(i+1,j)+helper(i,j+1) #函式呼叫函式
        return helper(0,0) #函式呼叫函式