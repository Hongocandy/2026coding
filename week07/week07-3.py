#week07-3.py 2390.
class Solution:
    def removeStars(self, s: str) -> str:
        ans=[] #用來放答案的陣列list 其實有stack性質
        for c in s: #逐一取出字母c 再判斷
            if c=='*': ans.pop() #遇到星號 吐掉一個字母
            else: ans.append(c) #把不是星號的字母 塞進去
        return ''.join(ans) #用單單.join()把陣列join成字串