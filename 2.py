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
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next

        return dummy.next


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
