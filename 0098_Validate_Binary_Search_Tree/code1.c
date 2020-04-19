/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int node;
bool temp;
int ans;
void preorder(struct TreeNode* ptr,int flag){
    if(ptr && temp==1){
        if(flag==1){
            if(ptr->val >= node){
                temp = 0;
            }
        }else{
            if(ptr->val <= node){
                temp = 0;
            }       
        }    
        preorder(ptr->left,flag);
        preorder(ptr->right,flag);       
    }
}

void isValid(struct TreeNode* root){  
    if(root && ans==1){
        node = root->val;
        temp = 1;
        preorder(root->left,1);
        if(!temp) ans = 0;

        node = root->val;
        temp = 1;
        preorder(root->right,2);            
        if(!temp) ans = 0;
  
        isValid(root->left);    
        isValid(root->right);    
    }
}

bool isValidBST(struct TreeNode* root){  
    ans = 1;
    isValid(root);
    return ans;
}
