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
    int widthOfBinaryTree(TreeNode* root) {
        int ans = 1;
        unordered_map<int, int> offest;
        recur(root, 0, 0, offest, &ans);
        return ans;
    }
    
    void recur(TreeNode* root, int depth, unsigned int target, unordered_map<int, int>& offest, int* ans){
        if(root == nullptr) {
            return;
        }
        
        if(offest.find(depth) == offest.end()) offest[depth] = target;

        target -= offest[depth];
        
        recur(root -> left, depth + 1, 2 * target, offest, ans);
        recur(root -> right, depth + 1, 2 * target + 1, offest, ans);  
        
        *ans = max(*ans, (int)target + 1);
    }
    
};