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
    int maxLevelSum(TreeNode* root) {
        
        queue<TreeNode*> q;
        q.push(root);
        
        int ans = 1;
        int maxSum = root -> val;
        int level = 1;
        
        while(!q.empty()){
            int sum = 0;
            queue<TreeNode*> next_q;
            while(!q.empty()){
                TreeNode* node = q.front(); q.pop();
                sum += node -> val;
                if(node -> left != nullptr){
                    next_q.push(node -> left);
                }
                if(node -> right != nullptr){
                    next_q.push(node -> right);
                }
            }
            if(maxSum < sum){
                maxSum = sum;
                ans = level;
            }
            
            level += 1;
            q = next_q;
        }
        
        return ans;
    }
};