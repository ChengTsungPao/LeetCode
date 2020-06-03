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
    int sum,left,right;
    void posorder(struct TreeNode* node){  
        if(node->left!=NULL){
            posorder(node->left);  
        }        
        if(node->right!=NULL){
            posorder(node->right);
        } 
        
        sum = 0; left = 0; right = 0;
        if(node->left!=NULL && node->left->val > 0){
            left = node->left->val;
        }        
        if(node->right!=NULL && node->right->val > 0){
            right = node->right->val;
        }       
        sum = left + right + node->val;
        if(sum > max){
            max = sum;
        }
        if(node->left!=NULL && node->right!=NULL){
            if(left > right){
                if(left > 0){
                    node->val += left;
                }
            }else{
                if(right > 0){
                    node->val += right;
                }
            }
        }else if(node->left==NULL && node->right!=NULL){
            if(right > 0){
                node -> val += right;
            }
        }else if(node->left!=NULL && node->right==NULL){
            if(left > 0){
                node -> val += left;
            }            
        }
       
    }
    posorder(root);

    return max;
}