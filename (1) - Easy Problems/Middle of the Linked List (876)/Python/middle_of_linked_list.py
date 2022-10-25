class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def middleNode(self, head: ListNode) -> ListNode:
        """
            While slow moves one step forward, fast moves two steps forward.
            When fast reaches the end, slow happens to be in the middle of the linked list.

            For example if head = [1, 2, 3, 4, 5]:
                                   v                          v
            1st Iteration: slow = [1, 2, 3, 4, 5], fast = [1, 2, 3, 4, 5]

                                      v                             v
            2nd Iteration: slow = [1, 2, 3, 4, 5], fast = [1, 2, 3, 4, 5]

                                         v                                v
            3rd Iteration: slow = [1, 2, 3, 4, 5], fast = [1, 2, 3, 4, 5]

            Since in the 3rd iteration fast would be outside the index,
            which in practical settings is not allowed, the while loop ends
            and the value of 'slow' is returned.
        """
        slow = fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow.val


sol = Solution()
print(sol.middleNode(ListNode([1, 2, 3, 4, 5])))
print(sol.middleNode(ListNode([1, 2, 3, 4, 5, 6])))
