#week14-3b.py 746.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N=len(cost)
        a=[0]*(N+1) #用來查表的表格
        a[0]=cost[0]
        a[1]=cost[1] #幸好題目有給
        for i in range(2,N+1):
            a[i]=min(a[i-1],a[i-2])
            if i<N:a[i]+=cost[i]
        return a[N]
        