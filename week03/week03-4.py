#week03-4.py 1004.


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros=0 #一開始的蛇蛇 肚子裡沒有0
        N=len(nums) #陣列的長度N
        ans=0 #床的 不會中毒而王的蛇蛇 長度是多少呢?
        tail=0 #尾巴一開始黏在0的位置 只有拉肚子十 才會往右縮
        for head in range(N): #蛇蛇的頭頭 慢慢往右吃
            if nums[head]==0: #吃到1個有毒的0
                zeros+=1 #身體內的毒素增加
                #if zeros>k: #超過身體可以容忍的上限 要拉肚子
                while zeros > k: #藥用while迴圈 一直拉肚子/排毒
                    if nums[tail]==0: #現在尾巴吐掉的是有毒的0
                      zeros-=1 #毒素減少!!
                    tail+=1 #尾巴拉肚子 拉完後不能留在髒髒的原地
            #排毒完畢 身體內保證不會有太多的有毒的0
            ans=max(ans,head-tail+1)
        return ans #最長的、不會中毒而死的蛇蛇 長度是ans