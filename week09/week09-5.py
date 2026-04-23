#week09-5.py 2095.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:return [] #很討厭的機車狀況 只有一個 避不掉
        prev=fast=slow=head #fast兔子 slow烏龜 一開始都在最前面

        while fast != None and fast.next != None: #兔子還沒到終點
            fast = fast.next.next #兔子跳兩格
            prev=slow #烏龜在走之前 先記下前一格的位置
            slow=slow.next #烏龜走一格
        #print(slow.val) #當兔子到終點時 烏龜在中間(沒錯)
        prev.next=slow.next
        return head
        