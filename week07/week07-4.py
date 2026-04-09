#week07-4.py 394.
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[] #利用stack處理方括號 及對應的數字
        nowN,nowS=0,'' #左邊now的數字 vs. 右邊nowS字串
        for c in s:
            if c.isdigit(): #如果是數字
               nowN=nowN*10+int(c)
            elif c.isalpha(): #如果是字母 就讓字串變長
               nowS+=c
            elif c=='[': #上括號:數字 字串 放入stack
               stack.append((nowN,nowS))
               nowN,nowS=0,'' #一組新的數字 字串
            elif c==']': #下括號 股出數字 字串
               prevN,prevS=stack.pop()
               nowS=prevS+prevN*nowS #重複的次數*字母
        return nowS