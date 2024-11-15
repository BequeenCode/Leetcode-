from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to make swapping easier
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy  # This will point to the node before the pair we're swapping
        
        # Iterate through the list in pairs
        while head and head.next:
            # Identify the two nodes to swap
            first = head
            second = head.next
            
            # Perform the swap by adjusting the pointers
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move the prev pointer to the first node (now the second node after the swap)
            prev = first
            
            # Move the head pointer to the next pair
            head = first.next
        
        # Return the new head (which is the node after dummy)
        return dummy.next
