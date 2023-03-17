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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        
        queue<TreeNode*> que;
        que.push(root);

        priority_queue<long long, vector<long long>, greater<long long>> pq;
        
        while(!que.empty()){
            int size = que.size();
            long long sum = 0;
            for(int i = 0; i < size; i++){
                TreeNode* node = que.front(); que.pop();
                sum += node -> val;
                
                if(node -> left){
                    que.push(node -> left);
                }
                if(node -> right){
                    que.push(node -> right);
                }
            }
            
            pq.push(sum);
            if(pq.size() > k) {
                pq.pop();
            }
            
        }
        
        return (pq.size() == k) ? pq.top() : -1;
    }
};