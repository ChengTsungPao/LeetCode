/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int sumNumbers(struct TreeNode* root){
    int ans = 0;
    void preorder(struct TreeNode* node, int number){
        if(node->left!=NULL){
            preorder(node->left, 10 * number + node->left->val);
        }
        if(node->right!=NULL){
            preorder(node->right, 10 * number + node->right->val);
        }  
        if(node->left==NULL && node->right==NULL){
            ans += number;
            return;
        }  
    }
    if(root!=NULL)
        preorder(root, root->val);        
    return ans;
}
