from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        while(head.next is not None):
            head.val = head.next
            print(head.val)

        # return number


sol = Solution()
print(sol.isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1))))))
