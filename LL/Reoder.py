# ⏱ Time Complexity:
# O(n) — single pass to build the array, then re-link

# 🧠 Space Complexity:
# O(n) — extra space to store nodes

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head:
        return

    # Step 1: Store all nodes in a list
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next

    # Step 2: Reorder using two pointers
    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]   # L0 → Ln
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]   # Ln → L1
        j -= 1

    # Step 3: Terminate the list
    nodes[i].next = None


# Input: 1 → 2 → 3 → 4 → 5

# Middle: 3

# Reversed second half: 5 → 4

# Merge:

# 1 → 5

# 5 → 2

# 2 → 4

# 4 → 3

# ✅ Final list: 1 → 5 → 2 → 4 → 3    

# ⏱ Time Complexity:
# O(n) — for finding middle, reversing, and merging

# 🧠 Space Complexity:
# O(1) — no extra space used

def reorderList(head):
    if not head or not head.next:
        return

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow.next
    slow.next = None  # Cut the list into two halves

    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Merge both halves
    first, second = head, prev
    while second:
        tmp1 = first.next
        tmp2 = second.next

        first.next = second
        second.next = tmp1

        first = tmp1
        second = tmp2