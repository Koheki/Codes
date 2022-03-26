# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def list2num(self,l):
        
        num = 0
        c = 0
        while l:
            num += int(l.val)*10**c 
            l = l.next
            c += 1
        return num
    
    
    def converted_num2list(self,num):
        
        
        ans = ListNode()
        
        while num > 0:
            # ans.append(num%10)
            n = num%10
            ans.val = n
            ans = ans.next
            
            num//=10
        
        return ans
    
    
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
#         n1 = self.list2num(l1)
#         n2 = self.list2num(l2)
        
#         return self.converted_num2list(n1+n2)


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        
        n1 = self.list2num(l1)
        n2 = self.list2num(l2)
        
        num = n1 + n2
        ans = ListNode()
    
        while num > 0:
            ans.val = 
 
            num//=10

        print(ans)
        
        # return self.converted_num2list(n1+n2)
            
        
        
    