/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseBetween(struct ListNode* head, int m, int n){
    int index = 1;
    int arr[n - m + 1];
    struct ListNode* temp = head;
    while(temp != NULL){
        if(index >= m && n >= index)
            arr[index - m] = temp -> val;
        index++;
        temp = temp -> next;
    }
    index = 1;
    temp = head;
    while(temp != NULL){
        if(index >= m && n >= index)
            temp -> val = arr[(n - m) - (index - m)];
        index++;
        temp = temp -> next;
    }
    return head;

}