/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


int maxPathSum(struct TreeNode* root){ 
    int max = INT_MIN;
    int localmax = INT_MIN;
    int tmp = 0;
    void preorder(struct TreeNode* node, int sum){  
        if(node->left!=NULL){
            preorder(node->left, sum + node->left->val);  
        }        
        if(node->right!=NULL){
            preorder(node->right, sum + node->right->val);
        } 
        if(sum > localmax){
            localmax = sum;
        }
        
    }
    void inorder(struct TreeNode* node){        
        if(node->left!=NULL){
            inorder(node->left);
        }
        
        //printf("value:%d\n",node->val);
        if(node->left!=NULL){
            preorder(node->left, 0 + node->left->val);
            if(localmax > 0){
                tmp += localmax;
            }
        }   
        localmax = INT_MIN;
        if(node->right!=NULL){
            preorder(node->right, 0 + node->right->val);
            if(localmax > 0){
                tmp += localmax;
            }
        }  
        tmp += node->val;
        if(tmp > max){
            max = tmp;
        }
        tmp = 0;        
        
        if(node->right!=NULL){
            inorder(node->right);
        }  
    }
    inorder(root);

    return max;
}
