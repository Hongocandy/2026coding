# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #方法一:神奇的bisect_left()寫法 只要一行
        #for i in range(1,n+1): pint(-guess(i),end=' ') #做個實驗 不用寫
        return bisect_left(range(n+1),0,key=lambda x:-guess(x)) #一行抵下面七行
        #for i in range(1,n+1): #錯誤的暴力法 for迴圈找答案
        #    if guess(i)==0:return i #猜中了 答案是i
        #不能用上面的for迴圈 因為n有20億這麼大 試不完
        #藥用小學猜數字 每次範圍猜一半 比它大比它小 縮小範圍
        left,right=1,n #左右的範圍(左包含 右不包含)
        while left<right: #左右的範圍還沒撞在一起
            mid=(left+right)//2 #(猜)中間的數字
            if guess(mid)==0: return mid #猜到中間的數字
            if guess(mid)>0: left=mid+1 #(暗示你)在高一點(中點設成下界)
            else:right=mid #(暗示你)在低點(中點設成上界)
        return left