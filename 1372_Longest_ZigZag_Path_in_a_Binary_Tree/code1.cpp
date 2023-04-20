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
    int longestZigZag(TreeNode* root) {
        int ans = 0;
        int left = recur(root -> left, 'L', &ans);
        int right = recur(root -> right, 'R', &ans);
        ans = max(ans, max(left, right) + 1); 
        return ans;
    }
    
    int recur(TreeNode* root, char parentD, int *ans) {
        if(root == nullptr){
            return -1;
        }
        
        int left = recur(root -> left, 'L', ans);
        int right = recur(root -> right, 'R', ans); 
        *ans = max(*ans, max(left + 1, right + 1));
        return (parentD == 'R') ? left + 1 : right + 1;
    }
};