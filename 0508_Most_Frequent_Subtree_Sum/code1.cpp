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
    unordered_map<int, int> status;
    
    vector<int> findFrequentTreeSum(TreeNode* root) {
        
        recur(root);
        
        int freq = INT_MIN;
        for(auto kv : status) {
            freq = max(freq, kv.second);
        } 
        
        vector<int> ans;
        for(auto kv : status) {
            if(kv.second == freq){
                ans.push_back(kv.first);
            }
        }         
        
        return ans;
    }
    
    int recur(TreeNode* node){
        if(!node){
            return 0;
        }
        
        int sum = node -> val + recur(node -> left) + recur(node -> right);
        if(status.find(sum) == status.end()){
            status[sum] = 1;
        } else {
            status[sum] += 1;
        }
        
        return sum;
    }
    
};