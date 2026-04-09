#week07-6.py 649.
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #print(list(senate)) #先印出senate
        #print(list(senate),type(list(senate))) #印出list(senate)
        #樓上兩行 印出字串 list(...) 下面印出deque(...)
        quene=deque(list(senate))
        #print(quene,type(quene)) #印出來 了解它是進階資料結構
        banR,banD=0,0 #目前被消滅的次數 都還是0
        R,D=senate.count('R'),senate.count('D') #目前有幾個人?

        while quene: #進行互相Ban對方的遊戲
            now=quene.popleft() #左邊吐出字母 他要消滅敵對陣營
            if now=='R': 
                if banR>0: #已經紀錄要消滅一個人
                   banR-=1 #用掉1個消滅的名額
                   R-=1 #馬上少掉一個人
                   #continue #你一出現 就已經被消滅了(換下一位)
                else: #你沒有被消滅 太好了 你可以反過來消滅對方
                    banD+=1
                    quene.append(now) #再到最右邊排隊
            else: #now=='D'
                if banD>0:
                    banD-=1
                    D-=1
                    #continue
                else:
                    banR+=1
                    quene.append(now)

            if R==0:return 'Dire' #把R消滅光 'D'就得勝
            if D==0:return 'Radiant' #把D消滅光 'R'就得勝
