#week12-3.py 547.
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N=len(isConnected) #先知道有幾個Nodes
        visited=set() #走過的地方不要再走

        def helper(now): #函式呼叫函式 因為function stack 也是一樣的DFS
            visited.add(now)
            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)
        ans=0 #有幾群是相連的
        for i in range(N): #全部nodes巡一次
            if i not in visited: #沒有去過的話 代表是新的一群
                ans+=1 #函式呼叫函式 暴力把她的鄰居、鄰居的鄰居、...全部走過
                helper(i)
        return ans

        