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
    int getMinimumDifference(TreeNode* root) {
        
        int ans = INT_MAX;
        int pre = -1;
        
        TreeNode* node = root;
        while(node != nullptr){
            if(node -> left == nullptr){
                ans = min(ans, (pre >= 0) ? node -> val - pre : INT_MAX);
                pre = node -> val;

                node = node -> right;
            } else {
                TreeNode* predecessor = node -> left;
                while(predecessor -> right != nullptr && predecessor -> right != node) {
                    predecessor = predecessor -> right;
                }
                
                if(predecessor -> right != node){
                    predecessor -> right = node;
                    node = node -> left;
                } else {
                    ans = min(ans, (pre >= 0) ? node -> val - pre : INT_MAX);
                    pre = node -> val;
                    
                    node = node -> right;
                    predecessor -> right = nullptr;
                }
            }
        }
        
        return ans;
    }
};