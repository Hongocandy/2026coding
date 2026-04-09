#week07-5.py 933.
class RecentCounter:

    def __init__(self):
        #使用Quene的資料結構 但python有constructions.deque
        #Double End Quene 簡稱 deque() 在Leetcode 可直接用它
        self.quene=deque() #宣告一個物件裡面是用slef找到的quene變數

    def ping(self, t: int) -> int:
        self.quene.append(t) #從右邊塞入1個數
        while self.quene[0]<t-3000: #目前最左邊 最古老的t 超過範圍
              self.quene.popleft() #Python的左邊吐掉
        return len(self.quene)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)