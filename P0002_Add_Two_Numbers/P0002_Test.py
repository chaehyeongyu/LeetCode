from P0002_Add_Two_Numbers import ListNode, Solution

head1 = ListNode(2)
curr = head1
new_node = ListNode(4)
curr.next = new_node
curr = new_node
new_node = ListNode(3)
curr.next = new_node

head2 = ListNode(5)
curr = head2
new_node = ListNode(6)
curr.next = new_node
curr = new_node
new_node = ListNode(4)
curr.next = new_node

solution = Solution()
sol = solution.addTwoNumbers(head1, head2)
while sol:
    print(sol.val)
    sol = sol.next

head1 = ListNode(0)
head2 = ListNode(0)

solution = Solution()
sol = solution.addTwoNumbers(head1, head2)
while sol:
    print(sol.val)
    sol = sol.next
    
head1 = ListNode(9)
curr = head1
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node

head2 = ListNode(9)
curr = head2
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node
curr = new_node
new_node = ListNode(9)
curr.next = new_node

solution = Solution()
sol = solution.addTwoNumbers(head1, head2)
while sol:
    print(sol.val)
    sol = sol.next
