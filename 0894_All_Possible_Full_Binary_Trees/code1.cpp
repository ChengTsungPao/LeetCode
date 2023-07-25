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
    vector<TreeNode*> allPossibleFBT(int n) {
        vector<vector<TreeNode*>> memo(n + 1, vector<TreeNode*>(0));
        return recur(n, memo);
    }
    
    vector<TreeNode*> recur(int n, vector<vector<TreeNode*>>& memo){
        if(!memo[n].empty()){
            return memo[n];
        }
        
        if(n == 1){
            return {new TreeNode(0)};
        }
                
        vector<TreeNode*> ans;
        for(int i = 1; i < n - 1; i++){
            for(TreeNode* left: recur(i, memo)){
                for(TreeNode* right: recur(n - i - 1, memo)){
                    TreeNode* root = new TreeNode(0);
                    root -> left = left;
                    root -> right = right;
                    ans.push_back(root);
                }
            }
        }
        return memo[n] = ans;
    }
    
};