# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        lsum = ListNode()
        curr_node = lsum
        while l1 or l2:
            if l1 and l2:
                curr_sum = l1.val + l2.val
                if curr_sum < 10:
                    new_node = ListNode(curr_sum)
                    curr_node.next = new_node
                    curr_node = new_node
                    l1 = l1.next
                    l2 = l2.next
                else:
                    new_node = ListNode(curr_sum-10)
                    if l1.next:
                        l1.next.val +=1
                    else:
                        l1.next = ListNode(1)
                    curr_node.next = new_node
                    curr_node = new_node
                    l1 = l1.next
                    l2 = l2.next
            elif l1:
                if l1.val < 10:
                    new_node = ListNode(l1.val)
                    curr_node.next = new_node
                    curr_node = new_node
                    l1 = l1.next
                else:
                    new_node = ListNode(l1.val-10)
                    if l1.next:
                        l1.next.val +=1
                    else:
                        l1.next = ListNode(1)
                    curr_node.next = new_node
                    curr_node = new_node
                    l1 = l1.next

            elif l2:
                if l2.val < 10:
                    new_node = ListNode(l2.val)
                    curr_node.next = new_node
                    curr_node = new_node
                    l2 = l2.next
                else:
                    new_node = ListNode(l2.val-10)
                    if l2.next:
                        l2.next.val +=1
                    else:
                        l2.next = ListNode(1)
                    curr_node.next = new_node
                    curr_node = new_node
                    l2 = l2.next
        return lsum.next
