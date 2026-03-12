#week03-3.py 1456.
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou') #把5個字母 變成set()
        #以後用if c in vowels:就可以快速確認他是母音
        #以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u'
        count=0 #紀錄目前有幾個母音
        for i in range(k): #找前面k個字母 逐一檢查 看是不是母音
            if s[i] in vowels: count+=1 #找到1個母音 開心!!!
        ans=count #離開迴圈時 確認前K個字母 有COUNT個母音 先當答案
        N=len(s) #鑽串的長度N
        for i in range(k,N): #右邊的每一個字母 逐一檢查
            if s[i] in vowels: count+=1 #右邊的頭s[i]右吃到一個母音
            if s[i-k] in vowels:count-=1 #左邊的尾巴s[i-1] 吐掉 失去一個母音
            ans=max(ans,count) #更新答案 找最大值
        return ans 
