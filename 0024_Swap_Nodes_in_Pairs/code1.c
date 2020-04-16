/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int inttmp;
struct ListNode* temp;
struct ListNode* swapPairs(struct ListNode* head){
    temp = head;
    while(temp && temp->next){
        inttmp = temp->val;
        temp->val = temp->next->val;
        temp->next->val = inttmp;
        temp = temp->next->next;
    }
    return head;
}