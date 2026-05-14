class Solution
    def canVisitAllRooms(self, rooms List[List[int]]) - bool
        stack=[0] #我們利用stack裡面待處理的房間 一開始房間是0是開的
        visited=set() #有去過、處理過的房間 不要再進去了
        visited.add(0) #已經排好、等待處理 下次有拿到鑰匙 不要再放入stack喽
        while stack #只要stack 裡還有東西 就繼續處理
              now=stack.pop() #吐出1個房間 現在要來處理
              for k in rooms[now] #把room now房間裡 所有的鑰匙k 都拿來做檢查
                  if k in visitedcontinue #鑰匙k對應的坊間k看過了 別再檢查
                  #如果走到這裡 代表沒走過、沒有待處理的房間k
                  stack.append(k) #加入stack資料結構
                  visited.add(k) #標記這個房間也待處理、其他人不要再排處理
        return len(rooms) ==len(visited) #房間的數目 全部都參觀過了 成功