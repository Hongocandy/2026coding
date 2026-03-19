#week04-4a.py 1732.
#找到最高的海拔高度(一直加就好)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=H=0
        for gg in gain:
            H+=gg
            ans=max(ans,H)
        return ans