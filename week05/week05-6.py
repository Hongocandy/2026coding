#week05-6.py 2352.
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter=Counter() #Hash Map可以知道有那些row出現幾次
        for row in grid: #每個row逐一處理
            counter[tuple(row)]+=1 #不會動的 才能把key放入Hash map
            #tuple() 可以把陣列[3,1,2,2],變不會動(3,1,2,2)
             
        ans=0 #有幾組?
        for col in zip(*grid): #矩陣 transpose 再取出col
            ans+=counter[tuple(col)] 
        return ans