/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* middleNode(struct ListNode* head){
    int index = 0;
    struct ListNode* temp = head;
    while(temp!=NULL){
        index++;
        temp = temp -> next;
    }
    for(int i = 0;i < index/2;i++)
        head = head -> next;
    return head;
}
