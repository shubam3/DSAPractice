class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:   
     prev_node = None
     curr_node = head  # Use 'head' directly

     while curr_node:  # Loop until we reach the end of the list
            next_node = curr_node.next  # Store next node
            curr_node.next = prev_node  # Reverse the pointer
            prev_node = curr_node  # Move prev_node forward
            curr_node = next_node  # Move curr_node forward

     return prev_node  # Return new head (previously the last node)
        