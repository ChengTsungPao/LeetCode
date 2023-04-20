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
        vector<int> target(1, 0);
        unordered_map<int, vector<vector<int>>> range;
        recur(root, 0, target, range, &ans);
        return ans;
    }
    
    void recur(TreeNode* root, int depth, vector<int> target, unordered_map<int, vector<vector<int>>>& range, int* ans){
        if(root == nullptr) {
            return;
        }
        
        recur(root ->  left, depth + 1,        mulTwo(target) , range, ans);
        recur(root -> right, depth + 1, addOne(mulTwo(target)), range, ans);
        
        int n = range[depth].size();
        
        if(n == 0){
            range[depth].push_back(target);
            range[depth].push_back(target);
        } else {
            range[depth][0] = minVector(range[depth][0], target);
            range[depth][1] = maxVector(range[depth][1], target);
        }
        
        *ans = max(*ans, sub(range[depth][1], range[depth][0]) + 1);
    }
    
    vector<int> addOne(vector<int> a){
        int n = a.size();
        
        int carry = 0;
        for(int i = 0; i < n; i++){
            a[i] += 1;
            if(a[i] < 10) break;
            carry = a[i] / 10;
            a[i] %= 10;
        }
        if(carry > 0) a.push_back(carry);
        return a;
    }
    
    vector<int> mulTwo(vector<int> a){
        int n = a.size();
        
        int carry = 0;
        for(int i = 0; i < n; i++){
            a[i] = 2 * a[i] + carry;
            carry = a[i] / 10;
            a[i] %= 10;
        }
        if(carry > 0) a.push_back(carry);
        return a;
    }
    
    vector<int> maxVector(vector<int> a, vector<int> b){
        int m = a.size();
        int n = b.size();
        
        if(m != n) return (m > n) ? a : b;
        
        for(int i = n - 1; i >= 0; i--){
            if(a[i] != b[i]) return (a[i] > b[i]) ? a : b;
        }
        return a;
    }
    
    vector<int> minVector(vector<int> a, vector<int> b){
        int m = a.size();
        int n = b.size();
        
        if(m != n) return (m < n) ? a : b;
        
        for(int i = n - 1; i >= 0; i--){
            if(a[i] != b[i]) return (a[i] < b[i]) ? a : b;
        }
        return a;
    }
    
    // a > b calculate a - b
    int sub(vector<int> a, vector<int> b){
        int m = a.size();
        int n = b.size();
        
        vector<int> result;
        int carry = 0, sub = 0;
        for(int i = 0; i < max(m, n); i++){
            if(i < m && i < n){
                sub = carry + a[i] - b[i];
            } else if (i < m) {
                sub = carry + a[i];
            } else if (i < n) {
                sub = carry - b[i];
            }
            
            result.push_back((sub + 10) % 10);
            carry = (sub < 0) ? -1 : 0;
        }
        
        int ans = 0, len = result.size();
        for(int i = len - 1; i >= 0; i--){
            ans = 10 * ans + result[i];
        }
        
        return ans;
    }
};