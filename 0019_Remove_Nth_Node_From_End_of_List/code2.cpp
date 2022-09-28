/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        
        ListNode* dummy = new ListNode(0, head);
        ListNode* pointeri = dummy;
        ListNode* pointerj = head;
        
        while(pointerj){
            if(n > 0){
                pointerj = pointerj -> next;
                n -= 1;
            } else {
                pointeri = pointeri -> next;
                pointerj = pointerj -> next;
            }
        }
        pointeri -> next = pointeri -> next -> next;
            
        return dummy -> next;
    }
};