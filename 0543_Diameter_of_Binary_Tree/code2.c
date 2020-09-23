/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int diameterOfBinaryTree(struct TreeNode* root){
    int max = 0;
    void posorder(struct TreeNode* node){
        if(node == NULL)
            return NULL;        
        posorder(node -> left);
        posorder(node -> right);          
        if(node -> left != NULL && node -> right != NULL){
            if(max < node -> left -> val + node -> right -> val)
                max = node -> left -> val + node -> right -> val;
            if(node -> left -> val > node -> right -> val)
                node -> val = node -> left -> val + 1;
            else
                node -> val = node -> right -> val + 1;
        }else if(node -> left != NULL){
            if(max < node -> left -> val)
                max = node -> left -> val;
            node -> val = node -> left -> val + 1;
        }else if(node -> right != NULL){
            if(max < node -> right -> val)
                max = node -> right -> val;
            node -> val = node -> right -> val + 1;
        }else
            node -> val = 1;
        return NULL;
    }

    posorder(root);       
    return max;
}