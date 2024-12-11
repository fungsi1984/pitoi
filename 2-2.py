from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sumList = ListNode()
        temp = sumList
        first = l1
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            res = val1 + val2 + carry
            carry = res // 10
            res = res % 10
            temp.next = ListNode(res)
            temp = temp.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return sumList.next

        # Helper function to create a linked list from a list of numbers


def create_linked_list(nums):
    dummy = ListNode(0)
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Helper function to print a linked list
def print_linked_list(l):
    nums = []
    while l:
        nums.append(l.val)
        l = l.next
    print(" -> ".join(map(str, nums)))


# Create linked lists for the numbers 342 and 465
l1 = create_linked_list([2, 4, 3])  # Represents the number 342
l2 = create_linked_list([5, 6, 4])  # Represents the number 465

# Create an instance of the Solution class
solution = Solution()

# Add the two numbers
result = solution.addTwoNumbers(l1, l2)

# Print the result
print_linked_list(result)  # Output should be 7 -> 0 -> 8 (representing the number 807)
