/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int kthSmallest(struct TreeNode* root, int k){
    int i = 0;
    int tmp;
    int inorder(struct TreeNode* node){        
        if(node->left!=NULL){
            tmp = inorder(node->left);
            if(tmp!=NULL){
                return tmp;
            }
        }
        i++;
        if(k==i){
            return node->val;
        }
        if(node->right!=NULL){
            tmp = inorder(node->right);
            if(tmp!=NULL){
                return tmp;
            }
        }  
        return NULL;
    }
    return inorder(root);  

}