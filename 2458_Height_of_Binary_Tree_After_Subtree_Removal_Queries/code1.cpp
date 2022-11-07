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

using umap_int = unordered_map<int, int>;
using umap_vec = unordered_map<int, vector<int>>;

class Solution {
public:
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        umap_int depths, heights;
        umap_vec top_height_val;
        umap_vec top_height;
        
        dfs(root, 0, depths, heights);

        for(auto [val, depth]: depths){
            int height = heights[val];
            int len = top_height[depth].size();
            
            if(len <= 1){
                top_height_val[depth].push_back(val);
                top_height[depth].push_back(height);
            } else if(height > top_height[depth][1]){
                top_height_val[depth][1] = val;
                top_height[depth][1] = height;
            }
            
            if(len + 1 >= 2 && top_height[depth][0] < top_height[depth][1]){
                swap(top_height_val[depth][0], top_height_val[depth][1]);
                swap(top_height[depth][0], top_height[depth][1]);
            }
        }
        
        vector<int> ans;
        for(auto val: queries){
            int depth = depths[val];
            int len = top_height[depth].size();
            if(val == top_height_val[depth][0]){
                ans.push_back(depth + ((len >= 2) ? top_height[depth][1] : -1));
            } else {
                ans.push_back(depth + top_height[depth][0]);
            }
        }
        
        return ans;
    }
    
    int dfs(TreeNode* root, int depth, umap_int& depths, umap_int& heights){
        if(root == nullptr){
            return -1;
        }
        
        int leftHeight = dfs(root -> left, depth + 1, depths, heights);
        int rightHeight = dfs(root -> right, depth + 1, depths, heights);
        int height = max(leftHeight, rightHeight) + 1;
        
        depths[root -> val] = depth;
        heights[root -> val] = height;

        return height;
    }
};