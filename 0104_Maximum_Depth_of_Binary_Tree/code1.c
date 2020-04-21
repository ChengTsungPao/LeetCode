/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root){
    int max = 0;
    void preorder(struct TreeNode* node){
        if(node->val > max){
            max = node->val;
        }
        if(node->left!=NULL){
            node->left->val = node->val + 1;
            preorder(node->left);
        }
        if(node->right!=NULL){
            node->right->val = node->val + 1;
            preorder(node->right);
        }  
    }
    if(root!=NULL){
        root->val = 1;
        preorder(root);       
    }
    return max;

}