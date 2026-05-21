#week13-1.py 1926.
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M,N=len(maze),len(maze[0]) #地圖迷宮地圖的長、寬
        visited=set() #用set()標示走過那些格子
        visited.add(tuple(entrance)) #走過的，不要再走，其中 tuple 很多逗號的座標
        quene=deque() #排隊、佇列
        quene.append((entrance[0],entrance[1],0)) #右邊塞入(i,j,第幾步)、排隊

        while quene:
            i,j,step=quene.popleft() #現在處理(i,j)
            for ii,jj in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                
                if ii<0 or jj<0 or ii>=M or jj>=N:continue #超過邊界 換下一位
                if maze[ii][jj]=='+':continue #遇到牆下一位
                
                if (ii,jj) not in visited: #沒到過這一格
                    if ii==0 or jj==0 or ii==M-1 or jj==N-1:return step+1 #找到出口
                    visited.add((ii,jj)) #標示這格已處理 排隊中 別重覆排隊
                    quene.append((ii,jj,step+1)) #真得排隊
        return -1
        