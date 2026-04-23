#week09-2.py 206.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while head:
            a.append(head.val)
            head=head=head.next #換下一筆
        #print(a)印出來 成功變成我們習慣的陣列a[i]
        now=ans=ListNode() #答案將串到裡面

        #下面用倒過來的迴圈 把陣列的值 逐一串到ans的後面
        N=len(a) #陣列的長度 要倒過來的迴圈
        for i in range(N-1,-1,-1):
            now.next=ListNode(a[i])
            now=now.next
        return ans.next
        