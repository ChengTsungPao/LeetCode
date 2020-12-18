# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = list(filter(lambda x: x != None, lists))
        length = len(lists)
        pointer = ans = ListNode()
        while len(lists) > 1:
            index = lists.index(min(lists, key = lambda x: x.val))
            before = pointer
            pointer.val = lists[index].val
            pointer.next = ListNode()
            pointer = pointer.next
            if lists[index].next == None:
                del lists[index]
            else:
                lists[index] = lists[index].next
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        else:
            before.next = lists[0]
            return a