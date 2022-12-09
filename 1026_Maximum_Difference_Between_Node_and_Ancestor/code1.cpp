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
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        recur(root, ans);
        return ans;
    }
    
    tuple<int, int> recur(TreeNode* root, int& ans){
        if (root -> left == nullptr && root -> right == nullptr){
            return make_tuple(root -> val, root -> val);
        } 
        
        tuple<int, int> tuple1 = (root -> left  != nullptr) ? recur(root -> left,  ans) : make_tuple(0, 100000);
        tuple<int, int> tuple2 = (root -> right != nullptr) ? recur(root -> right, ans) : make_tuple(0, 100000);
        int _max = max(get<0>(tuple1), get<0>(tuple2));
        int _min = min(get<1>(tuple1), get<1>(tuple2));
        
        ans = max(ans, max(abs(root -> val - _max), abs(root -> val - _min))); 
        return make_tuple(max(root -> val, _max), min(root -> val, _min));      
    }
};