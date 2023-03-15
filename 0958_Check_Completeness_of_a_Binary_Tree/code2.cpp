/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isCompleteTree(TreeNode* root) {
        
        queue<TreeNode*> que;
        que.push(root);
        
        int layerNum = 1;
        while(!que.empty()){
            
            bool isValid = true;
            int k = que.size();
            for(int i = 0; i < k; i++){
                TreeNode* node = que.front(); que.pop();
                
                if(node -> left){
                    if(!isValid) return false;
                    que.push(node -> left);
                } else {
                    isValid = false;
                }
                
                if(node -> right){
                    if(!isValid) return false;
                    que.push(node -> right);
                } else {
                    isValid = false;
                }
            }
            
            if(k != layerNum && que.size() > 0){
                return false;
            }
            layerNum *= 2;
        }
        
        return true;
    }
};