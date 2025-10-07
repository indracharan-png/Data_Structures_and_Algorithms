from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return head

        prev_node_ptr = None # Set up a pointer pointing to an empty node (None) of linkedlist
        curr_node_ptr = head # Set up pointer pointing to start node of linkedlist

        # Run through linkedlist till current node points to a None/null
        while(curr_node_ptr != None):
            # Store the next node respective to current node info 
            next_node_ptr = curr_node_ptr.next
            # Change the current node next pointer to previous node
            curr_node_ptr.next = prev_node_ptr
            # Update the previous node to current node
            prev_node_ptr = curr_node_ptr
            # Update the current node to next node (from stored info)
            curr_node_ptr = next_node_ptr
        
        return prev_node_ptr