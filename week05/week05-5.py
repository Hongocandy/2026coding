#week05-5.py 1657.
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1=Counter(word1) #統計用過的字母 出現的次數
        counter2=Counter(word2)
        #過的字母 是否是相同的集合(左邊有 右邊也會有)
        if set(counter1.keys())!=set(counter2.keys()): #用的字母不同就失敗
            return Fasle 
        #把出現的次數 小到大排好 如果兩邊都一樣 那就可以匯到一樣為止
        if sorted(counter1.values()) != sorted(counter2.values()): #次數不同
            return False
        return True