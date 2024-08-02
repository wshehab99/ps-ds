class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        carry=0
        result = ListNode(0)
        pos=result
        while l1 or l2 or carry:
            value1=l1.val if l1 else 0
            value2=l2.val if l2 else 0

            val = value1+value2+carry
            carry = val//10
            val =val%10
            pos.next = ListNode(val)
            

            pos = pos.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None 
        return result.next

            

    
solution = Solution()
print(solution.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))),ListNode(5,ListNode(6,ListNode(4)))))