#week07-2.cpp 735.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans=[]
        for a in asteroids:
            if a>0: #正的往左 不會跟左邊的相撞
               ans.append(a) #直接塞()
            else: #負的往左 可能會跟ans裡的東西相撞很多次
                while ans and ans[-1]>0: #目前有存 且最右邊是正的 向右會相撞
                    if abs(ans[-1])==abs(a): #絕對值大小都相同 都消滅
                        ans.pop() #消滅了 吐掉
                        a=0
                        break #離開迴圈
                    elif abs(ans[-1])>abs(a): #右邊比較小 消滅右邊
                        a=0 #消滅右邊
                        break
                    else: #左邊比較小 消滅左邊
                        ans.pop() #消滅 吐掉(這裡不用break)
                if a!=0: ans.append(a)
        return ans