#  Time Complexity: O(n)
# Reason:

# Move fast pointer n steps → O(n)

# Then move both fast and slow to the end → at most O(n)

# → Total: O(n)

# 🧠 Space Complexity: O(1)
# No extra space used (just pointers)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Step 1: Create dummy node
    dummy = ListNode(0, head)
    slow = fast = dummy

    # Step 2: Move fast ahead by n steps
    for _ in range(n):
        fast = fast.next

    # Step 3: Move both until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Step 4: Remove the node
    slow.next = slow.next.next

    # Return the updated list
    return dummy.next
