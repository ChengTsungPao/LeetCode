/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* headodd;
struct ListNode* headeven;
struct ListNode* tempodd;
struct ListNode* tempeven;
struct ListNode* oddEvenList(struct ListNode* head){
    if(head){
        headodd = head;
        headeven = head->next;
        tempodd = headodd;
        tempeven = headeven;
        while(headodd->next && headeven->next){
            headodd->next = headodd->next->next;
            headodd = headodd->next;
            headeven->next = headeven->next->next;
            headeven = headeven->next;
        }
        headodd->next = tempeven; 
        return tempodd;
    }
    return head;

    
}