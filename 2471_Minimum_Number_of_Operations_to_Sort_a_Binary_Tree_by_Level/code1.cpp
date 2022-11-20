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
    int minimumOperations(TreeNode* root) {
        
        int ans = 0;
        
        vector<TreeNode*> stack;
        stack.push_back(root);
        
        while(stack.size() > 0){
            vector<TreeNode*> next_stack;
            vector<int> vals;
            for(TreeNode* node: stack){
                vals.push_back(node->val);
                if(node->left != nullptr){
                    next_stack.push_back(node->left);
                }
                if(node->right != nullptr){
                    next_stack.push_back(node->right);
                }
            }
            stack = next_stack;
            ans += countSwap(vals);
        }
        
        return ans;
    }
    
    int countSwap(vector<int> vals){
        int n = vals.size();
        vector<int> sorted_vals = vals;
        sort(sorted_vals.begin(), sorted_vals.end());
        
        unordered_map<int, int> sorted_vals_index;
        for(int i = 0; i < n; i++){
            sorted_vals_index[sorted_vals[i]] = i;
        }
        
        int count = 0;
        for(int i = 0; i < n; i++){
            if(vals[i] != sorted_vals[i]){
                int j = sorted_vals_index[vals[i]];
                swap(sorted_vals[i], sorted_vals[j]);
                sorted_vals_index[sorted_vals[i]] = i;
                sorted_vals_index[sorted_vals[j]] = j;
                count += 1;
            }
        }        
        
        return count;
    }
    
};