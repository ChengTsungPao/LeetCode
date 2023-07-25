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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverse(l1);
        l2 = reverse(l2);
        
        ListNode* dummy = new ListNode();
        ListNode* cur = dummy;
        
        int c = 0;
        while(l1 != nullptr && l2 != nullptr){
            int d = l1 -> val + l2 -> val + c;
            c = d / 10;
            d %= 10;
            cur -> next = new ListNode(d);
            cur = cur -> next;
            
            l1 = l1 -> next;
            l2 = l2 -> next;
        }
        while(l1 != nullptr){
            int d = l1 -> val + c;
            c = d / 10;
            d %= 10;
            cur -> next = new ListNode(d);
            cur = cur -> next;
            
            l1 = l1 -> next;
        }
        while(l2 != nullptr){
            int d = l2 -> val + c;
            c = d / 10;
            d %= 10;
            cur -> next = new ListNode(d);
            cur = cur -> next;
            
            l2 = l2 -> next;
        }
        cur -> next = (c == 1) ? new ListNode(c) : NULL;
        
        return reverse(dummy -> next);   
    }
    
    ListNode* reverse(ListNode* head){
        if(head -> next == nullptr){
            return head;
        }
        
        ListNode* pre = head;
        ListNode* cur = head -> next;
        head -> next = nullptr;
        
        while(cur){
            ListNode* tmp = cur -> next;
            cur -> next = pre;
            pre = cur;
            cur = tmp;
        }
        
        return pre;
    }
    
};