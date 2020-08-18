/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* temp;
struct ListNode* oddEvenList(struct ListNode* head){
    if(head){
        temp = head;
        int length = 0;
        while(temp){
            length++;
            temp = temp->next;
        }       
        int data[length]; 
        temp = head;
        for(int i=0;i<length;i++){
            data[i] = temp->val;
            temp = temp->next;
        }
        temp = head;    
        for(int i=0;i<length;i+=2){
            temp->val = data[i];
            temp = temp->next;
        }
        for(int i=1;i<length;i+=2){
            temp->val = data[i];
            temp = temp->next;
        }
    }
    return head;
}